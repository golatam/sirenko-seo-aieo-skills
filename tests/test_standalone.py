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


if __name__ == '__main__':
    unittest.main()
