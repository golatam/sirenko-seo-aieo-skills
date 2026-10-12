"""Offline CLI/relocation tests. Every input and URL is synthetic."""
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
VALIDATOR = ROOT / 'skills/seo-aieo/scripts/validate_pack.py'
AI = ROOT / 'skills/aieo-visibility/scripts/summarize_observations.py'
FIXTURE = ROOT / 'skills/aieo-visibility/templates/synthetic-observations.jsonl'
EXTERNAL = {'competitor-analysis', 'humanizer-ru'}


class PortableCLITests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(dir=os.environ['TMPDIR'], prefix='seo-pack-test-')
        self.addCleanup(self.tmp.cleanup)
        self.scratch = Path(self.tmp.name)

    def run_script(self, path, *args):
        return subprocess.run([sys.executable, '-B', str(path), *map(str, args)], cwd=self.scratch,
                              env=dict(os.environ, PYTHONDONTWRITEBYTECODE='1'),
                              capture_output=True, text=True, timeout=30)

    def test_default_validator_from_foreign_cwd(self):
        p = self.run_script(VALIDATOR)
        self.assertEqual(p.returncode, 0, p.stderr + p.stdout)
        data = json.loads(p.stdout)
        self.assertEqual((data['requested'], data['checked']), (13, 13))
        self.assertEqual(data['errors'], [])
        self.assertEqual(data['warnings'], [])
        self.assertEqual(set(data['external_skills_declared']), EXTERNAL)
        self.assertFalse(data['external_availability_verified'])
        self.assertEqual(len({s['name'] for s in data['skills']}), 13)

    def test_explicit_manifest_and_skill_root(self):
        p = self.run_script(VALIDATOR, '--root', ROOT / 'skills', '--external-dependencies', ROOT / 'docs/host-dependencies.json')
        self.assertEqual(p.returncode, 0, p.stderr + p.stdout)
        self.assertEqual(json.loads(p.stdout)['checked'], 13)

    def test_no_blanket_external_bypass(self):
        manifest = self.scratch / 'none.json'
        manifest.write_text(json.dumps({'schema_version': 1, 'external_skills': [], 'scope': 'Synthetic negative fixture'}))
        p = self.run_script(VALIDATOR, '--external-dependencies', manifest)
        self.assertEqual(p.returncode, 1, p.stderr)
        self.assertTrue(any('unknown related skill' in e for e in json.loads(p.stdout)['errors']))

    def test_invalid_manifest_cli(self):
        path = self.scratch / 'invalid.json'
        path.write_text('{broken}', encoding='utf-8')
        p = self.run_script(VALIDATOR, '--external-dependencies', path)
        self.assertEqual(p.returncode, 2)
        self.assertEqual(p.stdout, '')
        self.assertNotIn('Traceback', p.stderr)

    def test_relocated_copy_without_live_skills(self):
        moved = self.scratch / 'different-name'
        shutil.copytree(ROOT, moved, ignore=shutil.ignore_patterns('.git', '.venv', '__pycache__', '*.pyc'))
        p = self.run_script(moved / 'skills/seo-aieo/scripts/validate_pack.py')
        self.assertEqual(p.returncode, 0, p.stderr + p.stdout)
        data = json.loads(p.stdout)
        self.assertEqual(data['checked'], 13)
        self.assertTrue(all(Path(s['path']).is_relative_to(moved) for s in data['skills']))
        p = self.run_script(moved / 'scripts/check_package.py')
        self.assertEqual(p.returncode, 0, p.stderr + p.stdout)

    def test_scratch_install_shape_with_explicit_manifest(self):
        installed = self.scratch / 'host-skills'
        shutil.copytree(ROOT / 'skills', installed, ignore=shutil.ignore_patterns('__pycache__', '*.pyc'))
        p = self.run_script(installed / 'seo-aieo/scripts/validate_pack.py', '--external-dependencies', ROOT / 'docs/host-dependencies.json')
        self.assertEqual(p.returncode, 0, p.stderr + p.stdout)
        data = json.loads(p.stdout)
        self.assertEqual(data['checked'], 13)
        self.assertTrue(all(Path(s['path']).is_relative_to(installed) for s in data['skills']))

    def test_synthetic_v2_cli(self):
        p = self.run_script(AI, FIXTURE, '--domain', 'example.com', '--alias', 'Example Brand', '--allow-synthetic')
        self.assertEqual(p.returncode, 0, p.stderr)
        data = json.loads(p.stdout)
        self.assertEqual(data['schema_version'], 2)
        self.assertEqual(data['evidence_kind'], 'synthetic_only')
        self.assertGreater(data['unique_observations'], 0)
        self.assertTrue(all(g['synthetic'] for g in data['groups']))

    def test_synthetic_opt_in_is_required(self):
        p = self.run_script(AI, FIXTURE, '--domain', 'example.com', '--alias', 'Example Brand')
        self.assertEqual(p.returncode, 2)
        self.assertEqual(p.stdout, '')
        self.assertIn('synthetic', p.stderr)

    def test_runner_requires_explicit_tempdir(self):
        env = dict(os.environ)
        env.pop('TMPDIR', None)
        p = subprocess.run([sys.executable, '-B', str(ROOT / 'scripts/run_tests.py')],
                           cwd=self.scratch, env=env, capture_output=True, text=True, timeout=10)
        self.assertEqual(p.returncode, 2)
        self.assertIn('set TMPDIR', p.stderr)

    def test_runner_rejects_in_repo_writes(self):
        for tmp, report in ((ROOT, self.scratch / 'not-created'), (self.scratch, ROOT / 'not-created')):
            with self.subTest(tmp=tmp, report=report):
                p = subprocess.run([sys.executable, '-B', str(ROOT / 'scripts/run_tests.py'), '--report-dir', str(report)],
                                   cwd=self.scratch, env=dict(os.environ, TMPDIR=str(tmp)),
                                   capture_output=True, text=True, timeout=10)
                self.assertEqual(p.returncode, 2)
                self.assertFalse(report.exists())
                self.assertIn('outside the source repository', p.stderr)

    def test_static_scan_negative_patterns(self):
        moved = self.scratch / 'negative-fixture'
        shutil.copytree(ROOT, moved, ignore=shutil.ignore_patterns('.git', '.venv', '__pycache__', '*.pyc'))
        # Marker only, not an actual key. Split strings avoid self-matching this test's source.
        marker = '-' * 5 + 'BEGIN ' + 'PRIVATE KEY' + '-' * 5
        private_path = '/' + 'data' + '/synthetic-root'
        (moved / 'docs/synthetic-negative.md').write_text(marker + '\n' + private_path + '\n', encoding='utf-8')
        p = self.run_script(moved / 'scripts/check_package.py')
        self.assertEqual(p.returncode, 1, p.stderr)
        errors = json.loads(p.stdout)['errors']
        self.assertTrue(any('known secret-like pattern' in e for e in errors))
        self.assertTrue(any('host-specific absolute path' in e for e in errors))

    def test_static_scan_ignores_macos_sidecar_files(self):
        moved = self.scratch / 'sidecar-fixture'
        shutil.copytree(ROOT, moved, ignore=shutil.ignore_patterns('.git', '.venv', '__pycache__', '*.pyc'))
        (moved / '._README.md').write_bytes(b'\x00\x05\x16\x07binary-appledouble')
        p = self.run_script(moved / 'scripts/check_package.py')
        self.assertEqual(p.returncode, 0, p.stdout + p.stderr)

    def test_static_scan_still_rejects_other_binary_files(self):
        moved = self.scratch / 'binary-fixture'
        shutil.copytree(ROOT, moved, ignore=shutil.ignore_patterns('.git', '.venv', '__pycache__', '*.pyc'))
        (moved / 'notes.bin').write_bytes(b'\xff\xfe\x00\x00')  # UTF-16 BOM, invalid as UTF-8
        p = self.run_script(moved / 'scripts/check_package.py')
        self.assertEqual(p.returncode, 1, p.stdout + p.stderr)
        self.assertTrue(any('expected readable UTF-8 source' in e for e in json.loads(p.stdout)['errors']))

    def test_static_scan_still_rejects_forbidden_directories(self):
        moved = self.scratch / 'forbidden-fixture'
        shutil.copytree(ROOT, moved, ignore=shutil.ignore_patterns('.git', '.venv', '__pycache__', '*.pyc'))
        (moved / 'raw-audits').mkdir()
        (moved / 'raw-audits' / 'x.md').write_text('synthetic', encoding='utf-8')
        p = self.run_script(moved / 'scripts/check_package.py')
        self.assertEqual(p.returncode, 1, p.stdout + p.stderr)
        self.assertTrue(any('generated/private path' in e for e in json.loads(p.stdout)['errors']))

    def test_missing_support_skill_fails_package_check(self):
        moved = self.scratch / 'missing-support-fixture'
        shutil.copytree(ROOT, moved, ignore=shutil.ignore_patterns('.git', '.venv', '__pycache__', '*.pyc'))
        shutil.rmtree(moved / 'skills/claim-verification')
        p = self.run_script(moved / 'scripts/check_package.py')
        self.assertEqual(p.returncode, 1, p.stdout + p.stderr)
        self.assertTrue(any('exactly the 12 core skills' in e for e in json.loads(p.stdout)['errors']))

    def test_runner_context_rejected_before_step_scope(self):
        import yaml
        for scope in ('workflow', 'job'):
            with self.subTest(scope=scope):
                moved = self.scratch / ('invalid-context-' + scope)
                shutil.copytree(ROOT, moved, ignore=shutil.ignore_patterns('.git', '.venv', '__pycache__', '*.pyc'))
                workflow = moved / '.github/workflows/tests.yml'
                data = yaml.safe_load(workflow.read_text(encoding='utf-8'))
                target = data if scope == 'workflow' else data['jobs']['offline']
                target.setdefault('env', {})['TMPDIR'] = '${{ runner.temp }}'
                workflow.write_text(yaml.safe_dump(data), encoding='utf-8')
                p = self.run_script(moved / 'scripts/check_package.py')
                self.assertEqual(p.returncode, 1, p.stdout + p.stderr)
                self.assertTrue(any('runner context' in error for error in json.loads(p.stdout)['errors']))

    def test_offline_html_cli(self):
        source = self.scratch / 'synthetic.html'
        source.write_text('<!doctype html><html><head><title>SYNTHETIC</title></head><body><h1>Fixture</h1><a href="/next">Next</a></body></html>', encoding='utf-8')
        output = self.scratch / 'synthetic-evidence.json'
        p = self.run_script(ROOT / 'skills/technical-seo-audits/scripts/html_evidence.py', '--html', source,
                            '--url', 'https://example.com/', '--out', output)
        self.assertEqual(p.returncode, 0, p.stderr)
        data = json.loads(output.read_text(encoding='utf-8'))
        self.assertFalse(data['execution']['network_requests'])
        self.assertEqual(data['source']['mode'], 'offline_html')
        self.assertIsNone(data['not_measured']['indexed'])
        self.assertEqual(data['titles'][0]['text'], 'SYNTHETIC')


if __name__ == '__main__':
    unittest.main()
