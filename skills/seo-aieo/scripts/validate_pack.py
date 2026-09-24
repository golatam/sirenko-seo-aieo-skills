#!/usr/bin/env python3
"""Read-only structure validation of the portable SEO/AIEO skill pack. Needs PyYAML.

Does not load plugins, fetch the network, execute skill code, or modify skills.
"""
from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    raise SystemExit('PyYAML unavailable in this interpreter; use an existing approved environment. Do not auto-install.')

PACK = (
    'seo-aieo', 'seo-research-strategy', 'seo-content-operations',
    'technical-seo-audits', 'seo-site-architecture', 'seo-specializations',
    'aieo-visibility', 'seo-authority-promotion', 'seo-reporting-monitoring',
    'google-search-console-operations', 'rank-tracker-operations',
    'ga4-project-reporting',
)
LOCAL_REF = re.compile(r'(?<![\w/])((?:references|templates|scripts|assets)/[A-Za-z0-9_.\-/]+\.(?:md|py|jsonl|json|csv|html|yaml|yml|txt))')


def checked_names(values, label):
    if not isinstance(values, (list, tuple, set)) or any(
        not isinstance(value, str) or not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', value)
        for value in values
    ):
        raise ValueError(label + ' must be a list of exact skill names')
    if len(set(values)) != len(values):
        raise ValueError(label + ' contains duplicate names')
    return sorted(values)


def load_external_dependencies(path: Path) -> list[str]:
    data = json.loads(path.read_text(encoding='utf-8'))
    if not isinstance(data, dict) or set(data) != {'schema_version', 'external_skills', 'scope'}:
        raise ValueError('dependency manifest requires schema_version, external_skills and scope only')
    if type(data['schema_version']) is not int or data['schema_version'] != 1:
        raise ValueError('dependency manifest schema_version must be integer 1')
    if not isinstance(data['scope'], str) or not data['scope'].strip():
        raise ValueError('dependency manifest must explain its declaration-only scope')
    names = checked_names(data['external_skills'], 'external_skills')
    if set(names) & set(PACK):
        raise ValueError('bundled skills cannot be declared external')
    return names


def validate(root: Path, names: list[str], external_skills=()) -> dict:
    external = checked_names(external_skills, 'external_skills')
    if set(external) & set(PACK):
        raise ValueError('bundled skills cannot be declared external')
    errors, warnings, results = [], [], []
    index: dict[str, list[Path]] = {}
    for path in root.rglob('SKILL.md'):
        if any(part.startswith('.') for part in path.relative_to(root).parts):
            continue
        index.setdefault(path.parent.name, []).append(path)
    for name in names:
        matches = index.get(name, [])
        if len(matches) != 1:
            errors.append(f'{name}: expected one active skill, found {len(matches)}')
            continue
        skill_file = matches[0]
        folder = skill_file.parent
        text = skill_file.read_text(encoding='utf-8')
        parts = re.split(r'^---\s*$', text, maxsplit=2, flags=re.M)
        if len(parts) != 3 or parts[0].strip():
            errors.append(f'{name}: missing initial YAML frontmatter')
            continue
        try:
            meta = yaml.safe_load(parts[1])
            if not isinstance(meta, dict):
                raise ValueError('frontmatter must be a mapping')
            if meta.get('name') != name:
                raise ValueError('frontmatter name differs from directory')
            if not isinstance(meta.get('description'), str) or not meta['description'].strip():
                raise ValueError('non-empty description required')
            if not parts[2].strip():
                raise ValueError('body is empty')
            if not meta['description'].startswith('Use when '):
                warnings.append(f'{name}: trigger is not in Use when form')
            if len(text.splitlines()) > 200:
                warnings.append(f'{name}: main file exceeds 200 lines')
            related = checked_names(meta.get('metadata', {}).get('hermes', {}).get('related_skills', []), 'related_skills')
            for sibling in related:
                if sibling not in index and sibling not in external:
                    errors.append(f'{name}: unknown related skill {sibling}')
        except (yaml.YAMLError, ValueError, TypeError, AttributeError) as exc:
            errors.append(f'{name}: {exc}')
            continue
        file_count = 0
        for path in sorted(folder.rglob('*')):
            if not path.is_file() or '__pycache__' in path.parts:
                continue
            file_count += 1
            try:
                if not path.resolve().is_relative_to(folder.resolve()):
                    raise ValueError('file escapes skill directory')
                if path.suffix == '.md':
                    content = path.read_text(encoding='utf-8')
                    for ref in sorted(set(LOCAL_REF.findall(content))):
                        if not (folder / ref).is_file():
                            errors.append(f'{name}/{path.relative_to(folder)}: missing local reference {ref}')
                elif path.suffix == '.py':
                    compile(path.read_text(encoding='utf-8'), str(path), 'exec')
                elif path.suffix == '.json':
                    json.loads(path.read_text(encoding='utf-8'))
                elif path.suffix == '.jsonl':
                    for line_no, line in enumerate(path.read_text(encoding='utf-8').splitlines(), 1):
                        if line.strip():
                            json.loads(line)
                elif path.suffix == '.csv':
                    with path.open(encoding='utf-8-sig', newline='') as handle:
                        rows = list(csv.reader(handle))
                    if not rows or not rows[0] or len(set(rows[0])) != len(rows[0]):
                        raise ValueError('empty or duplicate CSV headers')
                    if any(len(row) != len(rows[0]) for row in rows[1:] if row):
                        raise ValueError('CSV row width differs from header')
            except (ValueError, SyntaxError, OSError) as exc:
                errors.append(f'{name}/{path.relative_to(folder)}: {exc}')
        results.append({'name': name, 'path': str(folder), 'files': file_count,
                        'main_lines': len(text.splitlines()), 'description': meta['description']})
    return {'status': 'pass' if not errors else 'fail', 'requested': len(names),
            'checked': len(results), 'skills': results, 'errors': errors, 'warnings': warnings,
            'external_skills_declared': external, 'external_availability_verified': False,
            'scope': 'static structure only; not behavioral, SEO-effectiveness or provider integration tests'}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[2],
                        help='skills directory; default is relative to this script, independent of cwd')
    parser.add_argument('--external-dependencies', type=Path,
                        help='explicit JSON declaration of host skills; default: <root>/../docs/host-dependencies.json if present')
    parser.add_argument('--names', nargs='+', default=list(PACK))
    args = parser.parse_args()
    if not args.root.is_dir():
        parser.error('skill root does not exist')
    manifest = args.external_dependencies
    if manifest is None:
        candidate = args.root.parent / 'docs' / 'host-dependencies.json'
        manifest = candidate if candidate.is_file() else None
    try:
        external = load_external_dependencies(manifest) if manifest is not None else []
        result = validate(args.root, args.names, external_skills=external)
    except (OSError, ValueError) as exc:
        parser.error(str(exc))
    result['external_dependency_manifest'] = str(manifest) if manifest is not None else None
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result['status'] == 'pass' else 1


if __name__ == '__main__':
    sys.exit(main())
