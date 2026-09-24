# Technical SEO audit for Yandex

Use this reference when the target search engine is Yandex rather than Google. Apply the main skill's bounded crawl, evidence and approval rules first. UI labels/URLs below are navigation hints, not proof of current access or an exposed API; verify them in current official documentation and the actual property. Regional/content/local strategy belongs to `seo-specializations`.

All Site move/Reindex/Important pages additions, Metrica linking, Crawl by counters activation, robots/Clean-param changes and sitemap submissions are external writes: obtain explicit approval, then read back the exact target. Read-only audit never implies permission to submit. A bot UA string in logs is only a claim until identity is verified.

## Yandex-specific audit sequence

1. **Main mirror and migrations**
   - Probe HTTP/HTTPS and www/non-www.
   - Prefer direct 301/308 redirects for permanent canonical-host moves; record actual hops and intent. Multiple hops are an efficiency issue, not automatically failed indexing.
   - Verify **Site move** in Yandex Webmaster after host/protocol/domain changes.
   - Do not rely on the obsolete `Host` directive; use redirects and Webmaster migration controls.

2. **robots.txt for Yandex**
   - Check `User-agent: Yandex` and `User-agent: *` for conflicts.
   - Ensure important HTML/CSS/JS/media are crawlable.
   - Keep the absolute Sitemap URL current.
   - Use `Clean-param` only for query parameters that do not change meaningful content; never apply it to language, region, product/filter state, or other content-changing parameters.

3. **Sitemap and crawl state**
   - Check intended sitemap entries for preferred canonical 200 indexable URLs; record migration exceptions explicitly. Missing a robots Sitemap declaration alone is not an indexing blocker.
   - Compare bounded internal crawl URLs with enumerated Sitemap URLs and state coverage; not-reached URLs are only orphan candidates.
   - In Webmaster inspect **Crawl statistics**, **All pages / Pages in search**, selected canonicals, exclusion reasons, and crawl dates.
   - Distinguish: unknown URL → known but blocked/failing → crawled but excluded/duplicate.

4. **Important URLs**
   - Use **Check URL** for representative pages.
   - Record final URL, status, YandexBot access, meta robots, X-Robots-Tag, canonical, title/description/H1, rendered/HTML content, internal links, index state, and exclusion reason.
   - Use **Reindex pages** only after the underlying problem is fixed.
   - Add key URLs to **Important pages monitoring**.

5. **Yandex Metrica discovery**
   - If a verified counter exists, link it and inspect **Crawl by counters**.
   - This helps discovery but does not replace crawlability, Sitemap, or internal links.

6. **Regionality**
   - For geo-dependent businesses, verify the Webmaster region, real address/service area, contact consistency, and Yandex Business listing.
   - Regional landing pages need unique local value, not city-name substitution.

7. **Snippets and quality**
   - Validate structured data in Yandex Webmaster.
   - Review query impressions, clicks, CTR, positions, branded/non-branded splits, devices, and regions.
   - Inspect Site Quality Index (ИКС) as a diagnostic trend, not a direct ranking control.

## Priority

- **Critical:** YandexBot blocked, DNS/SSL/5xx failures, wrong mirror, noindex/wrong canonical on key pages, broken Sitemap, failed migration.
- **High:** parameter/mirror duplicates, orphaned key pages, wrong regionality, soft 404s, JS-only content/links.
- **Medium:** weak metadata, structured-data/snippet issues, links through redirects, false lastmod values.

## Official tools

- Sitemap: https://webmaster.yandex.ru/site/indexing/sitemap
- Crawl statistics: https://webmaster.yandex.ru/site/indexing/indexing
- All pages: https://webmaster.yandex.ru/site/indexing/all-pages
- Check URL: https://webmaster.yandex.ru/site/indexing/check-url
- Reindex: https://webmaster.yandex.ru/site/indexing/reindex
- Crawl by counters: https://webmaster.yandex.ru/site/indexing/crawl-metrika
- Important pages: https://webmaster.yandex.ru/site/indexing/url-tracker
- Regionality: https://webmaster.yandex.ru/site/serp-snippets/regions
- Diagnostics: https://webmaster.yandex.ru/site/optimization/checklist
- Quality: https://webmaster.yandex.ru/site/optimization/quality
- Structured data validator: https://webmaster.yandex.ru/site/tools/microtest
- Clean-param: https://yandex.ru/support/webmaster/ru/robot-workings/clean-param

## Output additions

A Yandex audit report should explicitly include:
- Webmaster/Metrica access status;
- target regions;
- known / crawled / indexed / excluded counts where available;
- top exclusion reasons;
- mirror and migration state;
- Clean-param and duplicate findings;
- query/CTR and ИКС observations;
- exact recheck method for every fix.
