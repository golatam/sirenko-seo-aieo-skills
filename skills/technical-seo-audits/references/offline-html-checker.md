# Offline HTML evidence checker

`scripts/html_evidence.py` is original stdlib-only Python, tested with Python 3.13. It processes one **local saved file**, not a site crawl. Use the skill directory (the directory the skill was loaded from; as a plugin: `skills/technical-seo-audits/` inside the plugin directory), not the shell cwd or another profile.

```bash
python3 <skill_dir>/scripts/html_evidence.py --html /path/source.html --url https://example.com/path --out /path/new-evidence.json
python3 -m unittest discover -s <skill_dir>/scripts -p 'test_html_evidence.py' -v
```

- `--url` is an absolute HTTP(S) document URL used for relative URL resolution only; no credentials/control characters.
- `--html` is a regular local input file. Default decoding `utf-8-sig` is strict; use `--encoding windows-1251` etc only when known from collection evidence. No guessed charset.
- `--out` must not exist or equal the input; parent directory must already exist. It refuses to overwrite. Exit 0 = evidence JSON written, **not an SEO pass**. Exit 2 = usage/input/output/budget error. Malformed JSON-LD is recorded in a successful evidence report, not treated as an execution error.
- Input/decode budget 5 MiB and 100,000 start elements are local resource limits, not Google limits. Budget exhaustion fails rather than silently reporting partial coverage.

Output includes source path, bytes, SHA-256, analysis timestamp (not fetch time), all metadata, titles/H1s with source lines, descriptions, duplicate tags/attributes, robots token observations scoped by name, canonicals, hreflang, first non-inert base-aware resolved anchor/area links, and JSON-LD raw blocks/parsed values/types/errors. Duplicate attributes retain raw pairs while the first value is used for convenience fields; duplicate JSON keys, non-JSON NaN/Infinity and numeric overflow beyond finite float range are parse errors. Parsed floating-point values can be rounded by Python; raw JSON remains available as the exact source.

## Interpretation and security

No JS/HTML execution, HTTP requests, DNS lookup, imports from input, shell commands, remote contexts or link fetching. Private and javascript: link strings can appear as **observed data**, never fetch targets. Treat output values as untrusted if embedded in any later HTML report; HTML-escape them there. Do not publish sensitive URLs, source files or token-bearing links unredacted.

This is `HTMLParser`, not an HTML5 DOM repair engine. It normalizes whitespace, preserves source observations and marks template/noscript elements inert. It cannot model CSS visibility, malformed browser tree construction, scripting-mode behavior, robots/header precedence or search-engine behavior. A tag outside head may be an invalid/ignored hint; `in_head` records explicit source context only (omitted head tags are not repaired). The first active base href is resolved against the document URL; an unsupported/invalid base produces a warning and documented URL fallback, not a claim of browser equivalence.

Known non-measurements are explicit nulls: HTTP status, response headers, robots.txt, indexing, rank, mobile speed/CWV, structured-data eligibility and rendered DOM. JSON parse success is not schema validation; source anchors are not complete crawl coverage. Multiple H1s alone are not a failure. No hidden numeric SEO score.

For comparisons, collect raw HTML and rendered DOM through separately authorized safe tools, record original URL/timestamp/status/device separately, then run each file to **new** output paths. The checker cannot tell whether a file was raw or rendered; label that in the audit evidence manifest.

## Test scope

Synthetic unittest fixtures cover duplicate title/description/canonical/H1/attributes; exact case-insensitive noindex/none vs lookalikes; first base and relative canonical/hreflang/links; good/malformed/duplicate-key/nonstandard JSON; inert markup; no-network guard; input URL/size/encoding failures; unclosed title; element budget; and real subprocess CLI JSON/overwrite safety. They prove these observations and safeguards, not real-world Google crawling, rendering or indexing. A separate public-page smoke test may demonstrate parsing a saved response, but is still not a full audit.
