# Schema, CWV, rendering, logs and indexing semantics

## Crawl ≠ index ≠ rank

Preserve the evidence ladder:

| Observation | What it supports | What it cannot establish |
|---|---|---|
| In sitemap/internal link | A discovery route exists | Engine fetched/indexed it |
| Audit GET 200 | Our client received a body now | Bot access, meaningful content or indexing |
| Verified crawler log hit | That crawler requested URL at timestamp | Index selection or actual citation |
| No observed noindex | One eligibility signal | Complete eligibility or indexing |
| Canonical tag | Publisher preference | Engine-selected canonical |
| Console URL inspection | Engine's recorded state at inspection/crawl date | Current live rendering or future ranking |
| Impressions/clicks | Visibility for reported dates and aggregation | Complete URL universe or full query set |

Do not call a page eligible solely from the offline tool. Headers, access, content, canonical consistency and engine evidence remain independent checks. Separate engine-specific data; don't average Google and Yandex index states.

## HTTP/header/meta semantics

- Record each redirect and final **GET** response; HEAD can differ. Keep repeated `X-Robots-Tag`/`Link` headers and UA scopes, not a dict that silently overwrites duplicates. Canonical/hreflang may be in HTTP Link headers or XML, not only HTML.
- Robots.txt controls crawling, not guaranteed removal. A disallowed page can still have its URL known/indexed; crawlers may not fetch it to see noindex. Do not propose disallow+noindex as an automatic removal recipe. Missing robots or Sitemap declaration is not intrinsically a block.
- Collect all applicable generic and engine-specific meta/header rules. Matching noindex isn't a substring search: tokenize case-insensitively, respect scope; `none` includes noindex/nofollow. `nofollow`, `nosnippet`, `max-snippet:0`, `noimageindex` and `indexifembedded` are not interchangeable with page noindex. Engine support differs; `index` does not override an applicable restrictive rule in Google. `data-nosnippet` restricts the marked text's snippet use, not page indexing.
- A canonical is a signal, not a redirect or instruction guaranteed to be honored. Cross-canonical duplicates can be intentional. Test target status, relevance, reciprocal consistency with sitemap/internal links, hreflang and selected canonical. A canonical to an unrelated category is not a general cure for a useful facet/page.
- Hreflang technical samples: absolute target URLs, supported language/region codes, reciprocal/self references where appropriate, equivalent content, canonical consistency, valid targets; x-default when justified. Validate language switcher via explicit mappings, not slug-prefix replacement. Full international strategy routes to `seo-specializations`.

Official reference: https://developers.google.com/search/docs/crawling-indexing/robots-meta-tag (checked 2026-09-24); recheck before engine-sensitive changes.

## JavaScript and mobile

Record initial HTTP headers/body and a rendered sample under explicit device/network/wait settings. Compare primary content, href graph, titles, H1, robots, canonical and structured data. Do not infer broken SEO from React/CSR detection alone. Test direct URL navigation/reload, not just clicking within the app; real 404/redirect semantics, client-router fallback 200s, hydration errors, resource blocking, user-interaction-dependent content and pagination are common failure classes.

Raw noindex must not rely on JS removal for recovery; conflicting canonicals or empty initial bodies warrant engine-specific checks. A browser DOM is not Googlebot's indexed DOM. GSC live test and last indexed version differ. Never say a page is mobile-friendly from a viewport tag; inspect content/action parity and layout. No screenshots or rendered checks available means those checks remain untested.

Official starting point: https://developers.google.com/search/docs/crawling-indexing/javascript/javascript-seo-basics . Dynamic rendering is a maintenance workaround, not a universal recommendation; choose SSR/SSG/hybrid from measured needs and engineering constraints.

## Structured data: four different validations

1. **Extraction/syntax:** preserve all JSON-LD blocks, raw parse errors, multiple types/@graph and duplicates; also inspect Microdata/RDFa when present. The bundled checker only parses JSON. JSON scalar/array parsing is not proof of usable JSON-LD.
2. **Vocabulary:** types, properties, IDs and relationships coherent with Schema.org? Syntax-valid is not schema-valid.
3. **Engine eligibility:** supported feature, required/recommended fields, page/content type, visibility and current policies; validate relevant Google types in Rich Results Test. JSON-LD is recommended, not the only supported format.
4. **Observed display:** only search/console evidence shows real rich-result appearance. Passing validators or valid markup does not guarantee display, ranking or AI citations.

Verify values against visible facts: price/currency/availability, author, dates, breadcrumbs, business identity; reject fake reviews, invented awards and hidden/unrelated markup. Use stable entity IDs and avoid conflicting duplicated organization/product definitions. Never globally delete valid markup solely because a Google feature was retired; other consumers may use it.

**Freshness rule:** before promising any feature, reopen the official gallery and its type guide; record checked date and exact source. Do not import donor FAQ/HowTo lore. As checked 2026-09-24, the gallery's actual feature table contains neither FAQ nor HowTo. Google's documentation updates explicitly state FAQ rich results stopped appearing May 7, 2026; older 'government/health only' advice is stale. Generated page summaries can still mention FAQs: use the actual table/update text, not summary metadata. HowTo absence from the current gallery is sufficient not to promise that Google feature; don't confuse it with removal of the Schema.org vocabulary.

Sources checked 2026-09-24:
- https://developers.google.com/search/docs/appearance/structured-data/search-gallery
- https://developers.google.com/search/docs/appearance/structured-data/sd-policies
- https://developers.google.com/search/updates#faq-deprecation

## CWV: field vs lab

Prefer field CrUX/RUM: identify URL vs origin fallback, device, date window, percentile and sample sufficiency. 'No field data' is unavailable, never pass/fail. Current checked targets: LCP ≤2.5s, INP ≤200ms, CLS ≤0.1 at the 75th percentile, with all three passing for a CWV pass. Do not present FID as the current metric.

Lighthouse/local traces are controlled **lab diagnostics**. Save tool/version, URL, device, throttling, cache state, timestamp and repeated-run spread. Lab LCP/CLS are not the field distribution; TBT is not INP. PSI may provide field and lab in one response: label the two sections, and never attribute origin-wide field data to a single URL. HTML size, inline JS or viewport are clues, not measured CWV/mobile speed.

Diagnose the measured bottleneck: TTFB, LCP resource discovery/priority, actual image transfer and responsive formats, render-blocking assets, long tasks/interaction handlers, unsized media/font/layout shifts and third-party cost. Choose fixes from the trace, not universal ordering. Verify comparable lab improvement and later field change separately; never promise ranking uplift.

Sources checked 2026-09-24: https://web.dev/articles/vitals ; https://developers.google.com/search/docs/appearance/core-web-vitals . Recheck metrics/thresholds before long-lived automation.

## Logs: claimed vs verified identity

With authorized server/CDN exports, preserve period/timezone, source layers, sampling ratio, missing days, fields and parser errors. Keep IPs/query tokens/private paths in protected artifacts; aggregate/redact report outputs. CDN edge hits may not appear in origin logs and vice versa; don't join them blindly or double count retries.

Aggregate by URL/template, response class, latency, time, bot claim and verification status; compare intended URLs, sitemap set, new URLs, redirects, 404/5xx and low-value parameter traffic. Denominators must state request count vs unique URLs. Correlate deployment/crawl changes without claiming causation from timing alone.

A `Googlebot`/`YandexBot`/AI UA string is **claimed**, not verified. Use each provider's current official IP-range or reverse-then-forward DNS procedure, with timestamp and outcome. Keep unverified/failed identity checks separate; do not trust arbitrary reverse DNS suffix strings alone. Search, training and user-triggered fetchers have different roles; consult current official bot docs and route AI-specific policy/visibility to the SEO/AIEO orchestrator. Crawl hits never prove training, citation, index inclusion or human traffic.
