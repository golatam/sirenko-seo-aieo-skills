# Migrations and incident recovery

## Migration contract

Input: change type (domain, protocol, CMS, URL structure, redesign), old/new origins, URL inventory sources, business-critical URLs, expected retained/merged/removed content, deploy owner, approval boundary and rollback capability. Do not rewrite working URLs merely for cosmetic SEO. Separate concurrent changes when possible to make diagnosis easier.

### Before deployment

1. Capture dated baseline: HTTP/redirect/robots/canonical/sitemap/hreflang, raw/rendered templates, field/lab performance, GSC/Webmaster states and organic conversions if authorized. Access missing stays missing.
2. Create `templates/migration-map.csv`: each known old URL has retain/move/merge/remove decision, intended target/status, reason and owner. Use real CMS/sitemap/crawl/log/GSC/inbound-link inventories; quantify omissions. Don't redirect all removed content to the homepage; keep real 404/410 when no replacement is relevant.
3. Validate mappings in code: duplicate old URLs, missing targets, cycles/chains, unintended many-to-one merges, unknown/unsafe hosts, query/encoding/trailing-slash rules, asset/PDF URLs and locale equivalents. Test catch-all rules with negative cases so nonmatching routes don't leak to unrelated pages.
4. Prepare destination pages, direct permanent redirects when appropriate, updated internal links, canonical/hreflang/schema and preferred sitemap. Keep staging access-controlled; ensure intended production pages won't inherit staging auth/robots/noindex. Never open private staging to our automated crawler; use approved local fixtures or a separately authorized engineering environment.
5. Stage and verify every mapping mechanically where feasible; document limits and sample high-value + each template + error cases. Review code/config diff, test collection, owner signoff and restore procedure. Take a versioned backup; confirm who can restore what and how quickly. Search-engine recrawl cannot be rolled back like a code deploy.

### Release gate and readback

No deployment, DNS/CDN/redirect/robots change, sitemap/indexing submission or Change of Address without explicit authorization for exact target and action. Keep credentials in approved tools, not files/chat. Use console moves only for eligible cases in current official docs, not every protocol/path change.

Write release gates before launch: critical mapped routes resolve to correct destination, no unintended noindex/auth/robots, no redirect loops, canonical/hreflang are consistent, retained functionality and analytics work. Define numeric availability/conversion guardrails from the site's baseline with owner; do not invent acceptable traffic-loss percentages.

After approved release, read **production** old and new URLs, redirect chains, final headers/body, robots and sitemap; test critical, ordinary, locale and negative cases. Check CDN caches/variants rather than only origin or staging. Read back console actions on the exact property, noting acceptance/pending status. A successful submission is not a successful migration or indexed result.

Retain old domain/DNS/TLS and redirects according to current official recommendations and user needs; Google's checked guide says generally at least a year for redirects, longer where useful. Monitor old and new hosts for crawl errors, canonicals, index selection, impressions/clicks and conversions at agreed intervals. Preserve changes alongside the baseline and coverage ledger. Index changes lag HTTP changes; do not keep flipping canonicals daily.

### Rollback

Stop expansion/release on failed gates. For an active outage, wrong canonical/noindex across critical templates, redirect loops or data-loss risk, notify owner and execute only the agreed rollback authorization. Restore known-good code/config/content/CDN rules, then re-read exact production failures. Restore consistency across links, canonicals, sitemaps and redirects; don't create reverse redirect loops while reverting a domain move. Record what cannot instantly revert (DNS caches, recrawl/index state). Retest business transactions only with separate permission and safe test accounts.

## Incident triage (traffic drop / deindexing / broken release)

1. Establish onset, engine/device/locale/page cohort and business symptom. Check analytics/tagging outages, consent changes, reporting delay/timezone and seasonality before declaring a ranking incident. Separate impression, CTR, position, conversion and tracking failures.
2. Preserve last-good/current evidence and change timeline. Check DNS/TLS/5xx/429, robots retrieval, WAF bot rules, accidental noindex/canonical, redirect errors, empty JS shells, missing content, sitemap drift and manual-action/security reports when authorized.
3. Classify confirmed cause, likely correlation and unknown. An algorithm-update date is context, not proof; no claims of penalty without relevant engine evidence. Do not request mass indexing as a substitute for fixing access/content.
4. Contain the confirmed failure: pause publishing, revert/patch the smallest responsible change with approval, preserve forensic artifacts for hacking incidents and route to security owner. Do not erase logs or regenerate everything.
5. Read back original URLs on production and compare matched control templates. Only after technical resolution, consider approved scoped recrawl/submission where supported; no indexing guarantee.
6. Track **technical recovery**, **verified recrawl**, **index selection**, **visibility**, **conversions** as separate milestones. Define recheck dates, owner and escalation conditions. Finish a short postmortem: evidence, root cause, impact cohort, fix, rollback, prevention test and remaining uncertainty.

Official migration guide, read 2026-09-24: https://developers.google.com/search/docs/crawling-indexing/site-move-with-url-changes . Recheck it for console move eligibility and retention guidance before executing a real migration.
