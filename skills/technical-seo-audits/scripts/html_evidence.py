#!/usr/bin/env python3
"""Offline HTML observations, not a crawler, DOM engine or SEO score.

Python stdlib only. Never fetches URLs or executes document content.
"""
import argparse
from collections import Counter
from datetime import datetime, timezone
import hashlib
from html.parser import HTMLParser
import json
import math
from pathlib import Path
import re
import sys
from urllib.parse import urljoin, urlsplit

MAX_BYTES = 5 * 1024 * 1024
MAX_ELEMENTS = 100000
ROBOT_NAMES = {'robots', 'googlebot', 'googlebot-news', 'bingbot', 'yandex'}


def document_url(value):
    try:
        p = urlsplit(value)
        if p.scheme not in ('http', 'https') or not p.hostname or p.username is not None or p.password is not None:
            raise ValueError('URL must be absolute HTTP(S) without credentials')
        _ = p.port
        if re.search(r'[\s\\\x00-\x1f\x7f]', value):
            raise ValueError('URL contains whitespace/control characters or backslashes')
    except ValueError as exc:
        raise ValueError('invalid document URL: ' + str(exc)) from exc
    return value


def strict_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError('duplicate JSON object key: ' + key)
        result[key] = value
    return result


def reject_constant(value):
    raise ValueError('non-JSON constant: ' + value)


def finite_float(value):
    number = float(value)
    if not math.isfinite(number):
        raise ValueError('JSON number exceeds finite float range: ' + value)
    return number


def json_types(value):
    types, queue = set(), [value]
    while queue:
        item = queue.pop()
        if isinstance(item, dict):
            value = item.get('@type', [])
            values = value if isinstance(value, list) else [value]
            types.update(x for x in values if isinstance(x, str))
            queue.extend(item.values())
        elif isinstance(item, list):
            queue.extend(item)
    return sorted(types)


class EvidenceParser(HTMLParser):
    def __init__(self, max_elements):
        super().__init__(convert_charrefs=True)
        self.max_elements = max_elements
        self.elements = 0
        self.in_head = False
        self.inert_depth = 0
        self.script = None
        self.captures = []
        self.result = {k: [] for k in ('titles', 'h1', 'metadata', 'descriptions', 'robots', 'canonicals', 'hreflang', 'bases', 'links', 'jsonld', 'html_attributes')}
        self.warnings = set()

    def handle_starttag(self, tag, attrs):
        self.elements += 1
        if self.elements > self.max_elements:
            raise ValueError('element budget exceeded; no partial report produced')
        names = Counter(k for k, _ in attrs)
        for key, count in names.items():
            if count > 1:
                self.warnings.add(f'duplicate_attribute:{tag}:{key}')
        a = {}
        for key, val in attrs:
            a.setdefault(key, val)
        if tag == 'head':
            self.in_head = True
        if tag in ('template', 'noscript'):
            self.inert_depth += 1
        pos = {'line': self.getpos()[0], 'in_head': self.in_head, 'inert': bool(self.inert_depth)}
        row = {**pos, 'attributes': attrs}
        if tag == 'html':
            self.result['html_attributes'].append(row)
        if tag in ('title', 'h1'):
            entry = {**row, 'text': ''}
            self.result['titles' if tag == 'title' else 'h1'].append(entry)
            self.captures.append((tag, entry))
        if tag == 'meta':
            row.update(name=a.get('name'), property=a.get('property'), content=a.get('content'))
            self.result['metadata'].append(row)
            name = (a.get('name') or '').lower()
            if name == 'description':
                self.result['descriptions'].append(row.copy())
            if name in ROBOT_NAMES:
                tokens = re.findall(r'[^\s,]+', (a.get('content') or '').lower())
                self.result['robots'].append({**row, 'scope': name, 'tokens': tokens, 'noindex_observed': bool({'noindex', 'none'} & set(tokens))})
        if tag == 'base' and 'href' in a:
            self.result['bases'].append({**row, 'href': a['href'] or ''})
        if tag == 'link':
            rel = (a.get('rel') or '').lower().split()
            entry = {**row, 'href': a.get('href'), 'rel': rel}
            if 'canonical' in rel:
                self.result['canonicals'].append(entry.copy())
            if 'alternate' in rel and 'hreflang' in a:
                self.result['hreflang'].append({**entry, 'hreflang': a['hreflang']})
        if tag in ('a', 'area') and 'href' in a:
            self.result['links'].append({**row, 'tag': tag, 'href': a['href'] or '', 'rel': (a.get('rel') or '').lower().split()})
        if tag == 'script':
            self.script = {'is_jsonld': (a.get('type') or '').strip().lower() == 'application/ld+json', 'raw': '', **row}

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        # HTML script/title/h1 are not void; this is a source parser, not DOM repair.
        self.handle_endtag(tag)

    def handle_data(self, data):
        if self.script is not None:
            if self.script['is_jsonld']:
                self.script['raw'] += data
            return
        for _, entry in self.captures:
            entry['text'] += data

    def finish_script(self, closed):
        if self.script and self.script['is_jsonld']:
            entry = self.script.copy()
            entry.pop('is_jsonld')
            entry['closed'] = closed
            try:
                parsed = json.loads(entry['raw'], object_pairs_hook=strict_object, parse_constant=reject_constant, parse_float=finite_float)
                entry.update(status='parsed', value=parsed, types=json_types(parsed))
            except (ValueError, RecursionError) as exc:
                entry.update(status='parse_error', error=str(exc), types=[])
            self.result['jsonld'].append(entry)
        self.script = None

    def handle_endtag(self, tag):
        if tag == 'script':
            self.finish_script(True)
        if tag == 'head':
            self.in_head = False
        if tag in ('template', 'noscript'):
            self.inert_depth = max(0, self.inert_depth - 1)
        self.captures = [(t, e) for t, e in self.captures if t != tag]

    def finish(self):
        self.close()
        # HTMLParser retains unterminated script text in rawdata.
        if self.script is not None:
            if self.script['is_jsonld']:
                self.script['raw'] += self.rawdata
            self.warnings.add('unclosed:script')
            self.finish_script(False)
        for tag, _ in self.captures:
            self.warnings.add('unclosed:' + tag)
        for key in ('titles', 'h1'):
            for row in self.result[key]:
                row['text'] = ' '.join(row['text'].split())


def resolve(base, href):
    if href is None:
        return {'resolved': None, 'scheme': None, 'resolution_error': 'missing href'}
    try:
        result = urljoin(base, href.strip())
        return {'resolved': result, 'scheme': urlsplit(result).scheme.lower()}
    except ValueError as exc:
        return {'resolved': None, 'scheme': None, 'resolution_error': str(exc)}


def analyze(html, url, max_elements=MAX_ELEMENTS):
    document_url(url)
    if len(html.encode('utf-8')) > MAX_BYTES:
        raise ValueError('decoded HTML exceeds 5 MiB UTF-8 budget')
    p = EvidenceParser(max_elements)
    p.feed(html)
    p.finish()
    d = p.result
    active_bases = [x for x in d['bases'] if not x['inert']]
    base = url
    if active_bases:
        candidate = resolve(url, active_bases[0]['href'])
        try:
            if re.search(r'[\s\\\x00-\x1f\x7f]', active_bases[0]['href'].strip()):
                raise ValueError('invalid characters in base href')
            base = document_url(candidate['resolved'] or '')
        except ValueError:
            p.warnings.add('unsupported_or_invalid_base_href; document URL fallback')
    for key in ('canonicals', 'hreflang', 'links'):
        for row in d[key]:
            row.update(resolve(base, row['href']))
    for key, label in (('titles', 'title_tags'), ('descriptions', 'description_tags'), ('canonicals', 'canonical_links'), ('bases', 'base_href_tags')):
        if len(d[key]) > 1:
            p.warnings.add('multiple_' + label)
    d.update(schema_version=1, document_url=url, resolution_base=base, elements_observed=p.elements,
             warnings=sorted(p.warnings), execution={'network_requests': False, 'javascript_executed': False, 'links_fetched': False},
             not_measured={k: None for k in ('http_status', 'response_headers', 'robots_txt', 'indexed', 'rank', 'mobile_speed', 'core_web_vitals', 'schema_eligibility', 'rendered_dom')},
             limitations=['HTMLParser source observations, not browser DOM/HTML conformance validation.', 'Tags in template/noscript are marked inert; scripting-mode behavior is not evaluated.', 'Robots tokens are observed only, not combined with headers or robots.txt.', 'JSON-LD parsed means JSON syntax only; no vocabulary, eligibility or rich-result validation.', 'Links are observed, never fetched; not a complete site inventory.'])
    return d


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--html', required=True, type=Path, help='Local HTML file; never a URL')
    ap.add_argument('--url', required=True, help='Document URL used only for resolving relative URLs')
    ap.add_argument('--out', required=True, type=Path, help='New local JSON path; existing files are refused')
    ap.add_argument('--encoding', default='utf-8-sig', help='Explicit decoding, default utf-8-sig; no charset guessing')
    args = ap.parse_args(argv)
    try:
        if args.html.resolve() == args.out.resolve():
            raise ValueError('input and output must differ')
        if not args.html.is_file():
            raise ValueError('input must be a regular local file')
        with args.html.open('rb') as f:
            raw = f.read(MAX_BYTES + 1)
        if len(raw) > MAX_BYTES:
            raise ValueError('input exceeds 5 MiB byte budget')
        result = analyze(raw.decode(args.encoding), args.url)
        result['source'] = {'mode': 'offline_html', 'path': str(args.html.resolve()), 'bytes': len(raw), 'sha256': hashlib.sha256(raw).hexdigest(), 'encoding': args.encoding, 'analyzed_at_utc': datetime.now(timezone.utc).isoformat(), 'fetched_at': None}
        payload = json.dumps(result, ensure_ascii=True, allow_nan=False, indent=2) + '\n'
        with args.out.open('x', encoding='utf-8') as f:
            f.write(payload)
        print(str(args.out))
        return 0
    except (OSError, ValueError, LookupError, RecursionError) as exc:
        print('html_evidence: ' + str(exc), file=sys.stderr)
        return 2


if __name__ == '__main__':
    sys.exit(main())
