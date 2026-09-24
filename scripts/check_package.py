#!/usr/bin/env python3
"""Bounded offline packaging checks, NOT an exhaustive secret/security audit."""
from __future__ import annotations

import argparse
import importlib.util
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
FORBIDDEN_PARTS = {'.git', '.venv', '__pycache__', 'node_modules', 'raw-audits', 'client-exports', 'reviewlogs'}
PRIVATE_PATH = re.compile(r'/(?:data|home|Users|tmp)/')
SECRET = re.compile(r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----|\bgh[pousr]_[A-Za-z0-9]{30,}|\bgithub_pat_[A-Za-z0-9_]{30,}|\bAIza[A-Za-z0-9_-]{30,}|\bsk-[A-Za-z0-9]{32,}')
EMAIL = re.compile(r'[A-Za-z0-9._%+-]+@([A-Za-z0-9.-]+\.[A-Za-z]{2,})')
LINK = re.compile(r'\[[^\]\n]+\]\(([^)\s]+)\)')
RESERVED_MAIL = {'example.com', 'example.net', 'example.org'}


def check(root: Path) -> dict:
    root = root.resolve()
    errors = []
    checked = 0
    # Git metadata and a local venv are operational, not package content.
    files = sorted(p for p in root.rglob('*') if not any(x in {'.git', '.venv'} for x in p.relative_to(root).parts))
    for p in files:
        rel = p.relative_to(root)
        if p.is_symlink():
            errors.append(f'{rel}: symlinks are not permitted in the portable distribution')
            continue
        if not p.is_file():
            continue
        checked += 1
        if any(x in FORBIDDEN_PARTS for x in rel.parts) or p.suffix in {'.pyc', '.pyo'}:
            errors.append(f'{rel}: generated/private path is not package content')
        if p.name == '.env' or p.name.startswith('.env.') or re.fullmatch(r'(?:credentials?|auth|tokens?)(?:\.[^.]+)?', p.name, re.I):
            errors.append(f'{rel}: credential-like filename')
            continue  # Do not inspect credential-file contents.
        try:
            text = p.read_text(encoding='utf-8')
        except (UnicodeError, OSError):
            errors.append(f'{rel}: expected readable UTF-8 source, not a binary artifact')
            continue
        if PRIVATE_PATH.search(text):
            errors.append(f'{rel}: host-specific absolute path')
        if SECRET.search(text):
            errors.append(f'{rel}: known secret-like pattern; inspect privately without printing value')
        for host in EMAIL.findall(text):
            if host.lower() not in RESERVED_MAIL and not host.lower().endswith(('.example', '.test', '.invalid')):
                errors.append(f'{rel}: non-example email address')
        if p.suffix == '.py':
            try:
                compile(text, str(rel), 'exec')
            except SyntaxError as exc:
                errors.append(f'{rel}: Python syntax error at line {exc.lineno}')
        if p.suffix == '.md':
            for link in LINK.findall(text):
                if re.match(r'^[a-z][a-z0-9+.-]*:', link, re.I) or link.startswith('#') or '<' in link or '$' in link:
                    continue
                target = (p.parent / link.split('#', 1)[0]).resolve()
                if not target.is_relative_to(root) or not target.exists():
                    errors.append(f'{rel}: missing/outside local Markdown link {link}')
                elif len(rel.parts) > 2 and rel.parts[0] == 'skills' and not target.is_relative_to(root / 'skills' / rel.parts[1]):
                    errors.append(f'{rel}: relative link leaves the independently installable skill package')
    spec = importlib.util.spec_from_file_location('pack_validator', ROOT / 'skills/seo-aieo/scripts/validate_pack.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    found = {p.parent.name for p in (root / 'skills').glob('*/SKILL.md')}
    if found != set(module.PACK):
        errors.append('skills/: exactly the 12 core skills are required')
    for required in ('README.md', 'LICENSE', 'SOURCES.md', 'requirements.txt', 'docs/DEPENDENCIES.md',
                     'docs/WORKSPACE.md', 'docs/SECURITY.md', 'docs/TESTING.md', 'docs/host-dependencies.json',
                     '.github/workflows/tests.yml'):
        if not (root / required).is_file():
            errors.append(f'missing package file: {required}')
    import yaml
    workflow = root / '.github/workflows/tests.yml'
    if workflow.is_file():
        data = yaml.safe_load(workflow.read_text(encoding='utf-8'))
        if data.get('permissions') != {'contents': 'read'}:
            errors.append('workflow must have exactly permissions contents: read')
        for job in data.get('jobs', {}).values():
            if 'permissions' in job and job['permissions'] != {'contents': 'read'}:
                errors.append('workflow job must not widen token permissions')
    return {'status': 'pass' if not errors else 'fail', 'files_checked': checked, 'errors': errors,
            'scope': 'Offline packaging, selected paths/patterns, Python compile and local Markdown links only. Not exhaustive secret detection or a security certification.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=ROOT)
    args = parser.parse_args()
    if not args.root.is_dir():
        parser.error('package root does not exist')
    result = check(args.root)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result['status'] == 'pass' else 1


if __name__ == '__main__':
    raise SystemExit(main())
