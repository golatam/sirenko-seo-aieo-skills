"""Guards that keep the pack self-contained and discoverable. Offline, stdlib + PyYAML."""
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
    r'|business-messaging-integrations|web-analytics-architecture', re.I)
TEXT_SUFFIXES = {'.md', '.py', '.json', '.csv', '.jsonl', '.yml', '.yaml', '.txt'}
SCANNED = ('skills', 'scripts', 'tests')


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


if __name__ == '__main__':
    unittest.main()
