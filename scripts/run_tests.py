#!/usr/bin/env python3
"""Run offline unit, CLI and packaging checks; no installs, host configuration or network calls."""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--report-dir', type=Path, help='new directory OUTSIDE this repository for exact logs/results')
    args = parser.parse_args()
    tmp = os.environ.get('TMPDIR')
    if not tmp or not Path(tmp).is_absolute() or not Path(tmp).is_dir():
        parser.error('set TMPDIR to an existing, approved, absolute scratch directory')
    if Path(tmp).resolve().is_relative_to(ROOT):
        parser.error('TMPDIR must be outside the source repository')
    report = args.report_dir.resolve() if args.report_dir else None
    if report:
        if report.is_relative_to(ROOT):
            parser.error('test reports must be outside the source repository')
        if report.exists():
            parser.error('report directory already exists; choose a new path to preserve previous evidence')
        report.mkdir(parents=True)
    env = dict(os.environ, TMPDIR=str(Path(tmp).resolve()), PYTHONDONTWRITEBYTECODE='1')
    stages = []
    suites = (
        ('validator-unit', 'skills/seo-aieo/scripts'),
        ('aieo-unit', 'skills/aieo-visibility/scripts'),
        ('html-unit', 'skills/technical-seo-audits/scripts'),
        ('portable-cli', 'tests'),
    )
    commands = [(name, [sys.executable, '-B', '-m', 'unittest', 'discover', '-s', str(ROOT / folder), '-p', 'test_*.py', '-v'], True)
                for name, folder in suites]
    commands += [
        ('structure', [sys.executable, '-B', str(ROOT / 'skills/seo-aieo/scripts/validate_pack.py')], False),
        ('package-static', [sys.executable, '-B', str(ROOT / 'scripts/check_package.py')], False),
    ]
    for name, command, unit in commands:
        try:
            process = subprocess.run(command, cwd=ROOT, env=env, capture_output=True, text=True, timeout=180)
            stdout, stderr, code = process.stdout, process.stderr, process.returncode
        except subprocess.TimeoutExpired:
            stdout, stderr, code = '', 'Stage timeout after 180 seconds\n', 124
        tests = re.search(r'Ran (\d+) tests? in ', stderr) if unit else None
        count = int(tests.group(1)) if tests else 0
        passed = code == 0 and (not unit or count > 0)
        stage = {'name': name, 'status': 'pass' if passed else 'fail', 'exit_code': code,
                 'tests': count, 'command': command}
        stages.append(stage)
        print(f'{name}: {stage["status"].upper()} (exit={code}, tests={count})', flush=True)
        if not passed:
            print(stdout + stderr, flush=True)
        if report:
            for suffix, value in (('stdout.log', stdout), ('stderr.log', stderr)):
                with (report / f'{name}.{suffix}').open('x', encoding='utf-8') as handle:
                    handle.write(value)
    result = {'status': 'pass' if all(s['status'] == 'pass' for s in stages) else 'fail',
              'python': sys.version.split()[0], 'unit_and_cli_tests': sum(s['tests'] for s in stages),
              'stages': stages,
              'scope': 'Offline unit/CLI/static checks, synthetic fixtures only. No provider access, network crawling, CMS write, hosted CI execution or SEO/business outcomes verified.'}
    payload = json.dumps(result, ensure_ascii=False, indent=2)
    if report:
        with (report / 'summary.json').open('x', encoding='utf-8') as handle:
            handle.write(payload + '\n')
    print(payload)
    return 0 if result['status'] == 'pass' else 1


if __name__ == '__main__':
    raise SystemExit(main())
