#!/usr/bin/env python3
"""Offline AI observation accounting. Stdlib only; never fetches evidence or calls a provider."""
import argparse
from collections import Counter, defaultdict
from datetime import datetime, timezone
import json
from pathlib import Path
import re
import sys
from urllib.parse import urlsplit


class ValidationError(ValueError):
    """Input cannot safely be summarized."""


TEXT_FIELDS = ('observation_id run_id panel_id panel_version prompt_id prompt_version prompt_text '
               'repeat_id engine model surface locale market intent observed_at evidence_ref').split()
ENUMS = dict(source_type={'ui','api','aggregator','simulated'}, search_mode={'auto','forced','off','unknown'},
             brand_scope={'branded','unbranded'}, status={'ok','error','unknown'})
FIELDS = set(TEXT_FIELDS) | set(ENUMS) | {'schema_version','search_used','error','raw_answer','mention',
    'mention_quote','recommendation','recommendation_quote','citations','exclusion_reason','synthetic','response_locale'}
CITATION_FIELDS = {'url','claim_quote','source_quote','fidelity','evidence_ref'}
FIDELITY = {'supported','partial','unsupported','unverifiable','not_reviewed'}
REVIEWED = {'supported','partial','unsupported'}
GROUP_FIELDS = ('panel_id panel_version engine model surface source_type search_mode locale market '
                'intent brand_scope synthetic').split()
CELL_FIELDS = GROUP_FIELDS + ['run_id','prompt_id','prompt_version','repeat_id']


def require(condition, message):
    if not condition:
        raise ValidationError(message)


def text(value):
    if not isinstance(value, str) or not value.strip():
        return False
    try:
        value.encode('utf-8')
    except UnicodeError:
        return False
    return True


def nullable_text(value):
    return value is None or text(value)


def domain_name(value):
    require(text(value) and value == value.strip(), 'domain must be a hostname without whitespace')
    require(not any(c in value for c in '/:@?#\\'), 'domain must not contain URL components')
    # Stdlib IDNA2003 maps distinct modern domains (e.g. ß -> ss).
    # Fail closed: ingestion must supply a verified ASCII/A-label host.
    require(value.isascii(), 'Unicode hostname requires a verified ASCII A-label; no lossy IDNA mapping')
    require(not value.endswith('..'), 'hostname has repeated trailing root dots')
    host = value.removesuffix('.').lower()
    require(len(host) <= 253 and '.' in host, 'hostname must have at least two labels')
    require(all(re.fullmatch(r'[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?', p) for p in host.split('.')),
            'invalid hostname label')
    return host


def url_host(url):
    require(text(url) and not re.search(r'[\s\\\x00-\x1f]',url), 'invalid citation URL')
    try:
        p = urlsplit(url)
        require(p.scheme in {'http','https'} and p.hostname is not None, 'citation URL must be absolute HTTP(S)')
        require(p.username is None and p.password is None, 'URL credentials forbidden')
        _ = p.port
        return domain_name(p.hostname)
    except ValueError as exc:
        raise ValidationError('invalid citation URL or hostname') from exc


def host_matches(url, domains, include_subdomains=False):
    host = url_host(url)
    return any(host == domain_name(d) or (include_subdomains and host.endswith('.'+domain_name(d))) for d in domains)


def alias_matches(quote, aliases):
    # Literal, Unicode-aware token boundaries; semantic entity adjudication remains manual.
    return any(re.search(r'(?<!\w)'+re.escape(a.casefold())+r'(?!\w)',quote.casefold()) for a in aliases)


def quoted_alias_matches(answer, quote, aliases):
    # Check every exact quote occurrence against its original surrounding chars.
    offset = 0
    while (start := answer.find(quote, offset)) != -1:
        end = start + len(quote)
        prefix = answer[max(0, start - 1):start].casefold()
        middle = quote.casefold()
        context = prefix + middle + answer[end:end + 1].casefold()
        for alias in aliases:
            pattern = r'(?<!\w)' + re.escape(alias.casefold()) + r'(?!\w)'
            if any(len(prefix) <= m.start() and m.end() <= len(prefix) + len(middle)
                   for m in re.finditer(pattern, context)):
                return True
        offset = start + 1
    return False


def no_duplicate_keys(pairs):
    out = {}
    for k,v in pairs:
        require(k not in out, 'duplicate JSON key: '+k)
        out[k] = v
    return out


def reject_constant(value):
    raise ValidationError('non-finite JSON number: '+value)


def canonical(value):
    return json.dumps(value,sort_keys=True,ensure_ascii=False,separators=(',',':'),allow_nan=False)


def validate(row, aliases, allow_synthetic):
    require(type(row) is dict, 'observation must be an object')
    # Reject escaped unpaired surrogates, including keys and nested evidence.
    canonical(row).encode('utf-8')
    require(set(row) == FIELDS, 'field mismatch: missing='+','.join(sorted(FIELDS-set(row)))+
            '; unknown='+','.join(sorted(set(row)-FIELDS)))
    require(type(row['schema_version']) is int and row['schema_version'] == 2,
            'schema_version must be integer 2; migrate v1 locale explicitly using the panel manifest')
    for field in TEXT_FIELDS:
        require(text(row[field]), field+' must be nonempty text')
    for field, choices in ENUMS.items():
        require(isinstance(row[field],str) and row[field] in choices, field+' has unknown value')
    require(type(row['synthetic']) is bool, 'synthetic must be boolean')
    require(not row['synthetic'] or allow_synthetic, 'synthetic rows require --allow-synthetic')
    require(row['source_type'] != 'simulated' or row['synthetic'], 'simulated requires synthetic=true')
    for field in ('search_used','mention','recommendation'):
        require(row[field] is None or type(row[field]) is bool, field+' must be true, false, or null')
    require(not (row['search_mode'] == 'off' and row['search_used'] is True), 'off mode contradicts search_used')
    require(re.fullmatch(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?(?:Z|[+-](?:[01]\d|2[0-3]):[0-5]\d)',row['observed_at']),
            'observed_at must be RFC3339 with timezone')
    try:
        stamp = datetime.fromisoformat(row['observed_at'].replace('Z','+00:00'))
    except ValueError as exc:
        raise ValidationError('invalid timestamp') from exc
    for field in ('error','raw_answer','mention_quote','recommendation_quote','exclusion_reason'):
        require(nullable_text(row[field]),field+' must be nonempty text or null')
    require(row['response_locale'] is None or (text(row['response_locale']) and
            re.fullmatch(r'[A-Za-z]{2,8}(?:-[A-Za-z0-9]{1,8})*', row['response_locale'])),
            'response_locale must be a language tag (mul for mixed, und for undetermined) or null')
    if row['status'] != 'ok':
        require(text(row['error']), 'error/unknown status needs a reason')
        require(all(row[f] is None for f in ('raw_answer','mention','mention_quote','recommendation',
                                            'recommendation_quote','citations','response_locale')), 'non-ok outcome must be unknown, not absence')
        return stamp, [], 0
    require(row['error'] is None and text(row['raw_answer']), 'ok needs raw_answer and null error')
    for field in ('mention','recommendation'):
        quote = row[field+'_quote']
        if row[field] is True:
            require(text(quote) and quote in row['raw_answer'], field+' quote not found in raw_answer')
        else:
            require(quote is None, field+' quote must be null when false or unknown')
    if row['mention'] is True:
        require(quoted_alias_matches(row['raw_answer'],row['mention_quote'],aliases),
                'mention quote lacks approved alias boundary in original answer context')
    if row['recommendation'] is True:
        require(row['mention'] is True, 'recommendation requires adjudicated entity mention')
    require(row['citations'] is None or type(row['citations']) is list, 'citations must be a list or null')
    citations, seen, duplicates = [], {}, 0
    for c in row['citations'] or []:
        require(type(c) is dict and set(c) == CITATION_FIELDS, 'invalid citation fields')
        url_host(c['url'])
        require(text(c['claim_quote']) and c['claim_quote'] in row['raw_answer'], 'claim_quote not in raw_answer')
        require(isinstance(c['fidelity'],str) and c['fidelity'] in FIDELITY, 'unknown fidelity')
        require(nullable_text(c['source_quote']) and text(c['evidence_ref']), 'invalid source evidence')
        if c['fidelity'] in REVIEWED:
            require(text(c['source_quote']), 'reviewed fidelity needs source_quote')
        key = (c['url'],c['claim_quote'])
        if key in seen:
            require(seen[key] == c, 'conflicting citation-claim judgments')
            duplicates += 1
        else:
            seen[key] = c
            citations.append(c)
    return stamp, citations, duplicates


def rate(numerator, denominator, unknown=0):
    return dict(numerator=numerator,denominator=denominator,unknown=unknown,
                rate=numerator/denominator if denominator else None)


def summarize(lines, domains, aliases, include_subdomains=False, allow_synthetic=False):
    domains = sorted(set(domain_name(d) for d in domains))
    require(domains and aliases and all(text(a) and a == a.strip() for a in aliases), 'domains and nonempty trimmed aliases required')
    groups = defaultdict(list)
    ids, cells, definitions = {}, {}, {}
    duplicates, total = 0, 0
    for line_number,line in enumerate(lines,1):
        total += 1
        try:
            row = json.loads(line,object_pairs_hook=no_duplicate_keys,parse_constant=reject_constant)
            stamp, citations, citation_duplicates = validate(row,aliases,allow_synthetic)
            encoded = canonical(row)
            if row['observation_id'] in ids:
                require(ids[row['observation_id']] == encoded, 'conflicting observation_id')
                duplicates += 1
                continue
            # A cell must identify exactly one attempt; corrected/retried observations need a new run/repeat.
            cell = tuple(row[f] for f in CELL_FIELDS)
            require(cell not in cells, 'duplicate measurement cell with different observation_id')
            prompt = tuple(row[f] for f in ('panel_id','panel_version','prompt_id','prompt_version'))
            definition = tuple(row[f] for f in ('prompt_text','locale','market','intent','brand_scope'))
            require(prompt not in definitions or definitions[prompt] == definition, 'prompt definition drift within panel version')
            definitions[prompt] = definition
            ids[row['observation_id']] = encoded
            cells[cell] = row['observation_id']
            state = 'unknown' if row['search_used'] is None else 'search' if row['search_used'] else 'no_search'
            key = tuple(row[f] for f in GROUP_FIELDS)+(stamp.astimezone(timezone.utc).date().isoformat(),state)
            groups[key].append((row,citations,citation_duplicates))
        except (ValueError,TypeError,KeyError,OverflowError) as exc:
            raise ValidationError(f'line {line_number}: {exc}') from exc
    result = []
    for key, entries in sorted(groups.items(),key=lambda item: canonical(item[0])):
        g: dict = dict(zip(GROUP_FIELDS+['date_utc','search_state'],key))
        eligible = [e for e in entries if e[0]['status']=='ok' and e[0]['exclusion_reason'] is None]
        g.update(observations=len(entries),eligible_answers=len(eligible),
                 errors=sum(e[0]['status']=='error' for e in entries),
                 unknown_status=sum(e[0]['status']=='unknown' for e in entries),
                 excluded=sum(e[0]['exclusion_reason'] is not None for e in entries),
                 exclusion_reasons=dict(Counter(e[0]['exclusion_reason'] for e in entries if e[0]['exclusion_reason'])),
                 duplicate_citations_removed=sum(e[2] for e in entries),
                 eligible_response_locales=dict(Counter(e[0]['response_locale'] or 'unknown' for e in eligible)))
        for metric in ('mention','recommendation'):
            known = [e[0][metric] for e in eligible if e[0][metric] is not None]
            g[metric] = rate(sum(known),len(known),len(eligible)-len(known))
        known_citations = [e for e in eligible if e[0]['citations'] is not None]
        matching = [[c for c in e[1] if host_matches(c['url'],domains,include_subdomains)] for e in known_citations]
        g['citation'] = rate(sum(bool(cs) for cs in matching),len(known_citations),len(eligible)-len(known_citations))
        fs = Counter(c['fidelity'] for cs in matching for c in cs)
        reviewed = sum(fs[f] for f in REVIEWED)
        pairs = sum(fs.values())
        g['fidelity_labels'] = {f:fs[f] for f in sorted(FIDELITY)}
        g['fidelity'] = rate(fs['supported'],reviewed,pairs-reviewed)
        g['fidelity_review_coverage'] = rate(reviewed,pairs)
        result.append(g)
    kinds = {g['synthetic'] for g in result}
    kind = 'empty' if not kinds else 'synthetic_only' if kinds=={True} else 'observed_only' if kinds=={False} else 'mixed_separate_groups'
    return dict(schema_version=2,evidence_kind=kind,input_rows=total,unique_observations=len(ids),
                exact_duplicates=duplicates,targets=dict(domains=domains,aliases=aliases,include_subdomains=include_subdomains),
                scope='Descriptive observed-attempt statistics only; no population, causal, traffic or consumer-UI inference from API data.',
                groups=result)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input',help='UTF-8 JSONL file, or - for stdin')
    parser.add_argument('--domain',action='append',required=True,help='exact owned hostname; repeat for approved aliases')
    parser.add_argument('--alias',action='append',required=True,help='literal approved brand alias; repeat as needed')
    parser.add_argument('--include-subdomains',action='store_true',help='explicitly include subdomains of approved hosts')
    parser.add_argument('--allow-synthetic',action='store_true',help='accept marked synthetic fixtures, isolated in output')
    args = parser.parse_args(argv)
    try:
        if args.input == '-':
            result = summarize(sys.stdin,args.domain,args.alias,args.include_subdomains,args.allow_synthetic)
        else:
            with Path(args.input).open(encoding='utf-8') as stream:
                result = summarize(stream,args.domain,args.alias,args.include_subdomains,args.allow_synthetic)
        payload = json.dumps(result,ensure_ascii=False,indent=2,allow_nan=False)
        payload.encode('utf-8')
        print(payload)
    except (OSError,UnicodeError,ValidationError,RecursionError) as exc:
        print(json.dumps({'error':str(exc)},ensure_ascii=True),file=sys.stderr)
        return 2
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
