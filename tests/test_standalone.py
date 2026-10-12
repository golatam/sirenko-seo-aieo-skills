"""Guards that keep the pack self-contained and discoverable. Offline, stdlib + PyYAML."""
import json
import re
import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
TRIGGER = 'Использовать, когда '


def frontmatter(path: Path) -> dict:
    parts = re.split(r'^---\s*$', path.read_text(encoding='utf-8'), maxsplit=2, flags=re.M)
    return yaml.safe_load(parts[1])


class DescriptionTests(unittest.TestCase):
    def test_every_skill_has_russian_trigger(self):
        skills = sorted((ROOT / 'skills').glob('*/SKILL.md'))
        self.assertEqual(len(skills), 13)
        for path in skills:
            with self.subTest(skill=path.parent.name):
                description = frontmatter(path)['description']
                self.assertIn(TRIGGER, description)
                self.assertLessEqual(len(description), 1024)
                self.assertRegex(description, r'[А-Яа-яЁё]')


HOST_NAMES = re.compile(
    r'hermes|clavito|openclaw|google-workspace|remote-mcp-oauth-operations'
    r'|business-messaging-integrations|web-analytics-architecture'
    r'|skill_view|skill_manage|web_extract|web_search|search_files|read_file|\bgateway\b', re.I)
TEXT_SUFFIXES = {'.md', '.py', '.json', '.csv', '.jsonl', '.yml', '.yaml', '.txt'}
SCANNED = ('skills', 'scripts', 'tests', 'docs', 'README.md', 'SOURCES.md', '.github')


class HostNeutralityTests(unittest.TestCase):
    def test_no_host_names(self):
        hits = []
        for entry in SCANNED:
            base = ROOT / entry
            files = sorted(base.rglob('*')) if base.is_dir() else [base]
            for path in files:
                rel = path.relative_to(ROOT)
                if (not path.is_file() or path.suffix not in TEXT_SUFFIXES or path.name.startswith('._')
                        or '__pycache__' in rel.parts or 'superpowers' in rel.parts or path == Path(__file__).resolve()):
                    continue
                for number, line in enumerate(path.read_text(encoding='utf-8').splitlines(), 1):
                    if HOST_NAMES.search(line):
                        hits.append(f'{rel}:{number}')
        self.assertEqual(hits, [], 'host-specific names remain:\n' + '\n'.join(hits[:30]))


class PluginManifestTests(unittest.TestCase):
    def load(self, name):
        return json.loads((ROOT / '.claude-plugin' / name).read_text(encoding='utf-8'))

    def test_plugin_and_marketplace_agree(self):
        plugin = self.load('plugin.json')
        market = self.load('marketplace.json')
        entry = market['plugins'][0]
        self.assertEqual(plugin['name'], 'seo-aieo')
        self.assertEqual(plugin['license'], 'MIT')
        self.assertEqual((entry['name'], entry['version'], entry['source']),
                         (plugin['name'], plugin['version'], './'))

    def test_readme_install_commands_match_manifests(self):
        plugin = self.load('plugin.json')
        market = self.load('marketplace.json')
        readme = (ROOT / 'README.md').read_text(encoding='utf-8')
        slug = plugin['repository'].removeprefix('https://github.com/')
        self.assertEqual(market['name'], 'sirenko-seo')
        self.assertIn(f'/plugin marketplace add {slug}', readme)
        self.assertIn(f"/plugin install {plugin['name']}@{market['name']}", readme)

    def test_skills_live_in_default_plugin_directory(self):
        self.assertTrue((ROOT / 'skills' / 'seo-aieo' / 'SKILL.md').is_file())


if __name__ == '__main__':
    unittest.main()
