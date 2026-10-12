"""Synthetic tests for static pack validation; no network or user data."""
import contextlib
import importlib.util
import io
import os
import tempfile
import unittest
from pathlib import Path

SPEC = importlib.util.spec_from_file_location('validate_pack', Path(__file__).with_name('validate_pack.py'))
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)

VALID = '---\nname: test-skill\ndescription: "Use when testing a skill."\n---\n# Test\nReal nonempty test body.\n'


class PackTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(dir=os.environ["TMPDIR"])
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.skill = self.root / 'productivity' / 'test-skill'
        self.skill.mkdir(parents=True)
        (self.skill / 'SKILL.md').write_text(VALID)

    def result(self):
        return MODULE.validate(self.root, ['test-skill'])

    def test_valid(self):
        self.assertEqual(self.result()['status'], 'pass')

    def test_missing(self):
        self.assertEqual(MODULE.validate(self.root, ['absent'])['status'], 'fail')

    def test_duplicate(self):
        other = self.root / 'another-category' / 'test-skill'
        other.mkdir(parents=True)
        (other / 'SKILL.md').write_text(VALID)
        self.assertEqual(self.result()['status'], 'fail')

    def test_name_mismatch(self):
        (self.skill / 'SKILL.md').write_text(VALID.replace('name: test-skill', 'name: wrong'))
        self.assertEqual(self.result()['status'], 'fail')

    def test_invalid_yaml(self):
        (self.skill / 'SKILL.md').write_text('---\nname: [broken\n---\n# Body\n')
        self.assertEqual(self.result()['status'], 'fail')

    def test_missing_reference(self):
        (self.skill / 'SKILL.md').write_text(VALID + '\nLoad `references/missing.md`.\n')
        self.assertEqual(self.result()['status'], 'fail')

    def test_existing_reference(self):
        (self.skill / 'references').mkdir()
        (self.skill / 'references' / 'exists.md').write_text('# Reference\n')
        (self.skill / 'SKILL.md').write_text(VALID + '\nLoad `references/exists.md`.\n')
        self.assertEqual(self.result()['status'], 'pass')

    def test_invalid_csv(self):
        (self.skill / 'templates').mkdir()
        (self.skill / 'templates' / 'bad.csv').write_text('a,b\n1,2,3\n')
        self.assertEqual(self.result()['status'], 'fail')

    def test_python_is_parsed_not_executed(self):
        (self.skill / 'scripts').mkdir()
        (self.skill / 'scripts' / 'not_run.py').write_text('raise RuntimeError("MUST NOT EXECUTE")\n')
        self.assertEqual(self.result()['status'], 'pass')

    def test_syntax_error(self):
        (self.skill / 'scripts').mkdir()
        (self.skill / 'scripts' / 'bad.py').write_text('def broken(:\n')
        self.assertEqual(self.result()['status'], 'fail')

    def test_python_compiler_constraints(self):
        (self.skill / 'scripts').mkdir()
        for text in ('return 1\n', 'break\n', 'nonlocal missing\n'):
            with self.subTest(text=text):
                (self.skill / 'scripts' / 'bad.py').write_text(text)
                self.assertEqual(self.result()['status'], 'fail')

    def test_invalid_json(self):
        (self.skill / 'templates').mkdir()
        (self.skill / 'templates' / 'bad.json').write_text('{invalid}')
        self.assertEqual(self.result()['status'], 'fail')

    def test_unknown_related_skill(self):
        changed = VALID.replace('---\n# Test', 'metadata:\n  seo:\n    related_skills: [absent]\n---\n# Test')
        (self.skill / 'SKILL.md').write_text(changed)
        self.assertEqual(self.result()['status'], 'fail')

    def test_explicit_external_dependency(self):
        changed = VALID.replace('---\n# Test', 'metadata:\n  seo:\n    related_skills: [host-example]\n---\n# Test')
        (self.skill / 'SKILL.md').write_text(changed)
        result = MODULE.validate(self.root, ['test-skill'], external_skills=['host-example'])
        self.assertEqual(result['status'], 'pass')
        self.assertEqual(result['external_skills_declared'], ['host-example'])
        self.assertFalse(result['external_availability_verified'])

    def test_external_typo_still_fails(self):
        changed = VALID.replace('---\n# Test', 'metadata:\n  seo:\n    related_skills: [host-exampel]\n---\n# Test')
        (self.skill / 'SKILL.md').write_text(changed)
        result = MODULE.validate(self.root, ['test-skill'], external_skills=['host-example'])
        self.assertEqual(result['status'], 'fail')
        self.assertTrue(any('host-exampel' in e for e in result['errors']))

    def test_bundled_skill_cannot_be_external(self):
        with self.assertRaises(ValueError):
            MODULE.validate(self.root, ['test-skill'], external_skills=['seo-aieo'])

    def test_related_must_be_name_list(self):
        for value in ('host-example', '[123]', '[host-example, host-example]'):
            with self.subTest(value=value):
                changed = VALID.replace('---\n# Test', f'metadata:\n  seo:\n    related_skills: {value}\n---\n# Test')
                (self.skill / 'SKILL.md').write_text(changed)
                self.assertEqual(MODULE.validate(self.root, ['test-skill'], external_skills=['host-example'])['status'], 'fail')

    def test_explicit_dependency_manifest(self):
        import json
        path = self.root / 'host-dependencies.json'
        path.write_text(json.dumps({'schema_version': 1, 'external_skills': ['host-example'], 'scope': 'Declaration only'}))
        self.assertEqual(MODULE.load_external_dependencies(path), ['host-example'])

    def test_invalid_dependency_manifest(self):
        import json
        path = self.root / 'host-dependencies.json'
        for data in (
            {'schema_version': 2, 'external_skills': [], 'scope': 'Declaration'},
            {'schema_version': 1, 'external_skills': ['seo-aieo'], 'scope': 'Declaration'},
            {'schema_version': 1, 'external_skills': ['x', 'x'], 'scope': 'Declaration'},
            {'schema_version': 1, 'external_skills': 'host-example', 'scope': 'Declaration'},
            {'schema_version': 1, 'external_skills': ['../unsafe'], 'scope': 'Declaration'},
            {'schema_version': 1, 'external_skills': [], 'scope': 'Declaration', 'ignore_all': True},
        ):
            with self.subTest(data=data), self.assertRaises(ValueError):
                path.write_text(json.dumps(data))
                MODULE.load_external_dependencies(path)

    def test_macos_sidecar_files_are_ignored(self):
        (self.skill / '._SKILL.md').write_bytes(b'\x00\x05\x16\x07binary-appledouble')
        result = self.result()
        self.assertEqual(result['status'], 'pass')
        self.assertEqual(result['skills'][0]['files'], 1)  # only SKILL.md counts

    def test_russian_trigger_description_accepted(self):
        text = VALID.replace('Use when testing a skill.', 'Проверка навыка. Использовать, когда просят «проверь навык».')
        (self.skill / 'SKILL.md').write_text(text)
        result = self.result()
        self.assertEqual(result['status'], 'pass')
        self.assertEqual(result['warnings'], [])

    def test_description_without_trigger_warns(self):
        (self.skill / 'SKILL.md').write_text(VALID.replace('Use when testing a skill.', 'A skill about testing.'))
        result = self.result()
        self.assertEqual(result['status'], 'pass')
        self.assertTrue(any('trigger' in w for w in result['warnings']))

    def test_description_too_long_fails(self):
        (self.skill / 'SKILL.md').write_text(VALID.replace('Use when testing a skill.', 'Use when testing. ' + 'x' * 1100))
        result = self.result()
        self.assertEqual(result['status'], 'fail')
        self.assertTrue(any('1024' in e for e in result['errors']))

    def test_support_skill_cannot_be_external(self):
        with self.assertRaises(ValueError):
            MODULE.validate(self.root, ['test-skill'], external_skills=['claim-verification'])

    def test_archive_is_not_active(self):
        other = self.root / '.archive' / 'test-skill'
        other.mkdir(parents=True)
        (other / 'SKILL.md').write_text(VALID)
        self.assertEqual(self.result()['status'], 'pass')


if __name__ == '__main__':
    unittest.main()
