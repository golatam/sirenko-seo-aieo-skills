"""Synthetic offline fixtures. No external site or search metric is tested."""
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

import html_evidence as checker

URL = 'https://example.org/docs/page'
FIXTURE = '''<!doctype html><html lang="en"><head>
<title>First &amp; title</title><title>Second</title>
<meta name="description" content="One"><meta name="description" content="Two">
<meta name="robots" content="INDEX, NoIndex, nofollow">
<meta name="googlebot" content="none">
<meta name="viewport" content="width=device-width">
<base href="/catalog/"><base href="https://ignored.example/">
<link rel="canonical" href="item"><link rel="canonical" href="/other">
<link rel="alternate" hreflang="es" href="../es/item">
<script type="application/ld+json">{"@context":"https://schema.org","@graph":[{"@type":"Article"}]}</script>
<script type="application/ld+json">{broken}</script>
</head><body><h1>Hello <span>world</span></h1><h1>Second</h1>
<a href="next#part">Next</a><a href="mailto:x@example.org">Mail</a>
<a href="javascript:alert(1)">Unsafe</a><a href="http://127.0.0.1/private">Private</a>
<script>fetch('https://never.example/')</script></body></html>'''


class EvidenceTests(unittest.TestCase):
    def test_duplicate_tags_preserved(self):
        d = checker.analyze(FIXTURE, URL)
        self.assertEqual([x['text'] for x in d['titles']], ['First & title', 'Second'])
        self.assertEqual([x['text'] for x in d['h1']], ['Hello world', 'Second'])
        self.assertEqual(len(d['descriptions']), 2)
        self.assertEqual(len(d['canonicals']), 2)
        self.assertIn('multiple_title_tags', d['warnings'])
        self.assertIn('multiple_canonical_links', d['warnings'])

    def test_noindex_tokens_and_scopes(self):
        d = checker.analyze(FIXTURE, URL)
        self.assertEqual(d['robots'][0]['tokens'], ['index', 'noindex', 'nofollow'])
        self.assertTrue(d['robots'][0]['noindex_observed'])
        self.assertTrue(d['robots'][1]['noindex_observed'])
        for token in ('noindexish', 'x-noindex', 'max-snippet:0', 'indexifembedded'):
            self.assertFalse(checker.analyze(f'<meta name="robots" content="{token}">', URL)['robots'][0]['noindex_observed'])

    def test_first_base_and_relative_links(self):
        d = checker.analyze(FIXTURE, URL)
        self.assertEqual(d['resolution_base'], 'https://example.org/catalog/')
        self.assertEqual(d['canonicals'][0]['resolved'], 'https://example.org/catalog/item')
        self.assertEqual(d['hreflang'][0]['resolved'], 'https://example.org/es/item')
        self.assertEqual(d['links'][0]['resolved'], 'https://example.org/catalog/next#part')
        self.assertEqual(d['links'][1]['scheme'], 'mailto')
        self.assertIn('multiple_base_href_tags', d['warnings'])

    def test_invalid_base_uses_document_fallback(self):
        for href in ('https://example.net:bad/path/', 'https://exa mple.net/path/',
                     'https://example.net:99999/path/', 'https://u:p@example.net/',
                     'https://example.net\\bad/path/', 'https://exa\u00a0mple.net/path/'):
            with self.subTest(href=href):
                d = checker.analyze(f'<head><base href="{href}"></head><a href="next">N</a>', URL)
                self.assertEqual(d['bases'][0]['href'], href)
                self.assertEqual(d['resolution_base'], URL)
                self.assertEqual(d['links'][0]['resolved'], 'https://example.org/docs/next')
                self.assertIn('unsupported_or_invalid_base_href; document URL fallback', d['warnings'])

    def test_jsonld_valid_malformed_and_strict(self):
        d = checker.analyze(FIXTURE, URL)
        self.assertEqual(d['jsonld'][0]['types'], ['Article'])
        self.assertEqual(d['jsonld'][0]['status'], 'parsed')
        self.assertEqual(d['jsonld'][1]['status'], 'parse_error')
        for body in ('{"x": NaN}', '{"x":1,"x":2}', '{"x": Infinity}', '{"x": 1e999}'):
            d = checker.analyze('<script type="application/ld+json">'+body+'</script>', URL)
            self.assertEqual(d['jsonld'][0]['status'], 'parse_error')

    def test_unclosed_json_and_link_resolution_edges(self):
        d = checker.analyze('<script type="application/ld+json">{"@type":"Thing"}', URL)
        self.assertEqual(d['jsonld'][0]['types'], ['Thing'])
        self.assertFalse(d['jsonld'][0]['closed'])
        self.assertIn('unclosed:script', d['warnings'])
        d = checker.analyze('<a href="../next">A</a><a href="//other.example/x">B</a><link rel="canonical"><a href="https://[bad">C</a>', URL)
        self.assertEqual(d['links'][0]['resolved'], 'https://example.org/next')
        self.assertEqual(d['links'][1]['resolved'], 'https://other.example/x')
        self.assertIsNone(d['canonicals'][0]['resolved'])
        self.assertIn('resolution_error', d['links'][2])

    def test_observation_not_execution_or_network(self):
        with patch('socket.socket', side_effect=AssertionError('network forbidden')):
            d = checker.analyze(FIXTURE, URL)
        self.assertFalse(d['execution']['network_requests'])
        self.assertFalse(d['execution']['javascript_executed'])
        self.assertEqual(d['links'][2]['scheme'], 'javascript')
        self.assertIn('http://127.0.0.1/private', [x['href'] for x in d['links']])
        for key in ('http_status', 'indexed', 'rank', 'mobile_speed', 'core_web_vitals', 'response_headers'):
            self.assertIsNone(d['not_measured'][key])

    def test_inert_markup_and_duplicate_attributes(self):
        d = checker.analyze('<head><template><base href="https://ignored.example/"><meta name="robots" content="noindex"></template><meta name="robots" name="googlebot" content="index"></head>', URL)
        self.assertEqual(d['resolution_base'], URL)
        self.assertTrue(d['robots'][0]['inert'])
        self.assertIn('duplicate_attribute:meta:name', d['warnings'])
        self.assertEqual(d['robots'][1]['scope'], 'robots')

    def test_bad_urls_unclosed_input_and_budget(self):
        for u in ('file:///etc/passwd', 'https://u:p@example.org/', 'https://@example.org/', 'relative', 'https://[bad'):
            with self.assertRaises(ValueError):
                checker.analyze('', u)
        d = checker.analyze('<title>Unclosed', URL)
        self.assertEqual(d['titles'][0]['text'], 'Unclosed')
        self.assertIn('unclosed:title', d['warnings'])
        with self.assertRaises(ValueError):
            checker.analyze('<a href="/">' * 6, URL, max_elements=5)


class CLITests(unittest.TestCase):
    def run_cli(self, *args):
        return subprocess.run([sys.executable, '-I', str(Path(checker.__file__).resolve()), *map(str,args)], capture_output=True, text=True, timeout=10)

    def test_cli_json_and_refuse_overwrite(self):
        with tempfile.TemporaryDirectory(dir=os.environ['TMPDIR']) as tmp:
            page, out = Path(tmp)/'fixture.html', Path(tmp)/'evidence.json'
            page.write_text(FIXTURE, encoding='utf-8')
            p = self.run_cli('--html', page, '--url', URL, '--out', out)
            self.assertEqual(p.returncode, 0, p.stderr)
            d = json.loads(out.read_text())
            self.assertEqual(d['source']['bytes'], len(FIXTURE.encode()))
            self.assertEqual(len(d['source']['sha256']), 64)
            self.assertEqual(d['source']['mode'], 'offline_html')
            before = out.read_bytes()
            self.assertEqual(self.run_cli('--html', page, '--url', URL, '--out', out).returncode, 2)
            self.assertEqual(before, out.read_bytes())
            self.assertEqual(self.run_cli('--html', page, '--url', URL, '--out', page).returncode, 2)
            self.assertEqual(page.read_text(), FIXTURE)

    def test_cli_missing_invalid_encoding_and_oversize(self):
        with tempfile.TemporaryDirectory(dir=os.environ['TMPDIR']) as tmp:
            page, out = Path(tmp)/'bad.html', Path(tmp)/'out.json'
            self.assertEqual(self.run_cli('--html', page, '--url', URL, '--out', out).returncode, 2)
            page.write_bytes(b'\xff')
            self.assertEqual(self.run_cli('--html', page, '--url', URL, '--out', out).returncode, 2)
            self.assertFalse(out.exists())
            with page.open('wb') as f:
                f.truncate(checker.MAX_BYTES + 1)
            self.assertEqual(self.run_cli('--html', page, '--url', URL, '--out', out).returncode, 2)
            self.assertFalse(out.exists())


if __name__ == '__main__':
    unittest.main()
