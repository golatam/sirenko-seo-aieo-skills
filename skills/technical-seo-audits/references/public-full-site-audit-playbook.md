# Bounded public full-site technical audit

Use when live read-only evidence is authorized; load the main skill first. Save artifacts in the project audit directory; use `$TMPDIR` for disposable probes, never hard-coded system temp paths.

## 1. Collection contract and safety

Record exact allowlisted public origins, entry points, engines/UA, time, purpose, collector version and budget. Conservative **operator defaults, not search-engine limits**: 100 HTML URLs, 10 rendered templates, 20 sitemap documents, recursion depth 3, 10,000 enumerated `<loc>` entries, 1 request/second/host, concurrency 1, 15-minute total deadline. Set separate limits for HTTP requests including redirects/robots/sitemaps and browser subresources; begin with 250 raw HTTP requests. Rendering consumes its own explicit page/resource/byte budget. Expand only deliberately and record why.

- Respect applicable robots rules, site terms and rate limits. Identify the audit UA honestly; label a bot-UA comparison as a simulation, not an actual Googlebot visit. Unavailable robots is unknown: use the crawler/engine-specific documented behavior, pause automated expansion rather than assuming access.
- Fetch only public HTTP(S), allowlisted hosts/ports. Reject userinfo, loopback, private, link-local, multicast, reserved and metadata-service destinations. Validate DNS results and redirect hops, not just the first hostname; prevent DNS-rebinding/TOCTOU in the chosen collector. Do not follow external canonical/hreflang/sitemap hosts automatically. No logged-in accounts, forms, cart/checkout, logout, admin, preview tokens or state-changing query URLs. Off-scope/private references may be recorded but never fetched.
- Enforce bounded redirects (e.g. 5), connect/read/overall timeouts, compressed and decompressed byte limits, URL/queue counts and query-pattern caps. Use a collector with these controls; if unavailable, inspect explicitly selected URLs manually rather than writing an unsafe crawler. Browser resource requests require equivalent network isolation; if unavailable, skip automated rendering of untrusted targets and report that limitation.
- Back off on 429 using Retry-After; pause on repeated 403/5xx, growing latency, robot denial or budget exhaustion. One bounded retry and one permitted alternative are enough; no WAF bypass or recursive retry loops. Authentication/errors from our environment are not automatically site defects.
- Do not assume requests, bs4, defusedxml, Chromium or Lighthouse exist. Check versions first; install only with permission in an isolated environment. Avoid unpinned `npx -y` and disabling browser sandbox by default.

## 2. Discovery and recursive sitemaps

GET canonical home and robots; test only relevant controlled host/protocol variants. Record each redirect, status and final URL. Discover Sitemap directives plus a bounded conventional `/sitemap.xml` fallback or supplied/GSC sitemap. A missing robots file or missing Sitemap directive is not itself an indexing block; valid discovery through another channel may suffice.

For `sitemapindex`, recurse through child locations within the same limits; for `urlset`, enumerate URLs. Support namespaces and `.gz`/Content-Encoding without double decompression. Keep seen sets to detect cycles/duplicates. Treat sitemap `<loc>` as untrusted: reject invalid/non-absolute/off-scope destinations for fetching, record them separately. Cross-host sitemaps can be legitimate with ownership context; do not declare them broken from host mismatch alone.

Use an entity-safe XML parser; disallow DTD/external entities and fail closed if safe parsing is unavailable. Bound compressed input (example 5 MiB), uncompressed output (example 10 MiB), nesting and total entries. Streaming gzip must stop at the decompressed limit, not allocate all content first. These **audit limits** can be below the protocol allowance: flag `not fully parsed: budget`, not `invalid sitemap`. Do not apply the 5 MiB HTML checker budget as a search-engine fetch limit. Record transport/parser errors separately.

Treat sitemap as a list of preferred canonical indexable URLs, not proof they are fetched/indexed. Record redirects, non-200, intended vs accidental noindex and canonical mismatches; verify a sample or full known set within budget. Check meaningful `lastmod`, not automatically refreshed dates. Never automatically regenerate/submit it in a read-only audit.

## 3. Coverage ledger and sampling

Persist URL rows and aggregate/deduplicate in code. Include: source membership (sitemap/internal/CMS/GSC/log), template/language, depth from named seed, attempted/completed, status/error, byte/time limits, rendered status, headers/meta/canonical and artifact paths. Report:

- unique discovered vs enumerated vs attempted vs fetched vs rendered;
- failed/skipped/robots-denied/off-scope/deferred and exact stop reason;
- known eligible universe per template and sampled count; unknown denominator stays unknown;
- unvisited frontier and sitemap children not parsed.

Seed important pages plus at least one ordinary and one edge case per relevant template; on large sites add reproducibly selected random samples with a saved seed. Include changes, high-value URLs, pagination/facets, locales and anomalies. If budget prevents representation, name the missing strata. Never extrapolate one template finding to all URLs without source/template evidence.

`crawl_seen - sitemap_urls` = observed URLs absent from the enumerated sitemap set, not automatically a defect. `sitemap_urls - crawl_seen` = **not reached in this bounded crawl**, not proven orphaned. Confirm orphan candidates against complete inventories, raw/rendered graphs and CMS before calling them orphans.

## 4. Raw vs rendered and page checks

Save raw HTTP body and headers separately. The rendered DOM must retain URL, timestamp, device, wait condition, browser version and errors; it is not the original server response or a faithful replica of Google's renderer. Compare titles/H1/content, canonical, robots, JSON-LD and anchor hrefs. A JS-only internal link is a dependency, not proof of exclusion. Critical metadata conflicting between initial HTML and rendering is more important than framework choice.

Capture status/redirects, title/description/H1 multiplicity, lang, viewport, canonicals, hreflang, images/alt/dimensions, link graph, schema, cache/security headers. Test bounded duplicate variants (slash, known tracking parameter, old URL) and one safe nonexistent path for soft-404 behavior. Missing CSP/HSTS is a security recommendation, not an invented direct ranking penalty. Non-HTML/PDF indexing requires headers and engine evidence; the HTML checker cannot do that.

## 5. Performance, CMS and operational checks

Load `schema-cwv-js-logs.md` for field/lab interpretation. If PSI is quota-limited and an approved local Lighthouse installation exists, use it on home mobile/desktop and representative listing/detail templates; otherwise mark performance unavailable. Save JSON and actual runtime flags/version. Repeat comparable lab runs; inspect LCP element, TTFB, payload, image transfers, TBT, CLS sources, render-blocking CSS, unused JS, third-party scripts and cache. Do not treat absent/removed Lighthouse audits as zeros, use old TTI as a required metric, or TBT as measured INP.

Tilda/JS-feed checks retained from earlier practice:
- Visual headings may be divs; inspect actual markup.
- Feed detail links may appear only after JS (including Tilda feeds); compare DOM before alleging orphaning, prefer useful HTML navigation fallback.
- Small-looking cards may load multi-megabyte originals: inspect actual network transfers, not dimensions alone.
- Service/menu/footer pages may intentionally be non-indexable; check intent before proposing sitemap inclusion.
- Audit corporate/feed templates separately for lang, metadata, author hrefs and uncreated category routes.

Inspect responsive layouts, content/action parity, intrusive overlays and accessibility using real browser observations, not just viewport metadata. Public RDAP expiry data can flag an operational risk, but imminent expiry alone is not P0: verify registration status/auto-renew with owner before claiming service loss. Review trust/contact/forms/privacy visibly; do not give definitive legal compliance verdicts from HTML.

## 6. Report and recheck

Use `templates/audit-evidence.md`. Put confirmed business-critical blockers first. P0=active severe incident, P1=high-impact confirmed defect, P2=optimization/quality improvement, P3=backlog; deadlines depend on owner capacity and dependencies, not automatic calendar promises. Include page inventory, exact broken edges, reproduction, confidence and unknown access. Public `site:`/SERP samples are not GSC index counts. Read back approved production fixes before calling them deployed; console recovery and traffic effects require later measured evidence.
