# Images / Video / News / Discover — separate surfaces

## Common gate

**Input:** page/asset inventory, rights/provenance, audience/task, publication workflow, renderer/CDN, authorized reporting and scope.
**Output:** [media-audit.md](../templates/media-audit.md), per-surface eligibility checklist, exact technical/content findings, DRAFT change set, read-back and measurement plan.
**Validation:** asset truthful and licensed; content accessible to users/crawlers as intended; structured data matches visible content; visibility evidenced on the actual surface, not inferred from a validator.
Do not assume every commercial site needs News or every product clip needs a separate watch page. Select relevant modules; record not-applicable reasons.
All upload/publish/sitemap/CMS changes and rights purchases require preview+confirmation+read-back. No copied copyrighted images, consent-free customer faces/voices, deceptive manipulated footage or invented captions.

## A. Images

**Input:** landing page, exact image/CDN URLs, selected variant/context, format/dimensions/size, alt/caption, license and metadata.
1. Verify the image depicts the actual claim/product; check rights, required attribution, model/property consent where relevant and derivative-use permission. Alt text does not replace licensing.
2. Inspect rendered HTML: discoverable `img src`/responsive fallback; CSS-only background cannot be assumed equivalent for indexing. Test CDN URL status, stable access and intended crawler permissions.[11]
3. Use concise descriptive alt for meaning/function, empty alt for purely decorative images when appropriate; no keyword stuffing. Caption/source around the image provides context. Keep essential instructions in text, not only pixels.
4. Optimize responsive dimensions/compression without unreadable diagrams. Test visual/crop correctness and main-image loading/performance; no universal format/number rule.
5. Assess image sitemap for assets hard to discover; validate current supported extension fields and absolute accessible URLs before drafting. An image sitemap aids discovery, not guaranteed indexing.[11]
6. If licensing/creator metadata or AI provenance is required by the platform, use verified source information and current feature docs. Do not fabricate copyright ownership or license URLs.
**Output/validation:** asset ledger + page/asset fetch evidence + accessibility review + proposed sitemap/metadata; verify actual rendered image after approval. Compare image-search reporting separately from web search; file requests alone are not visitors.

## B. Video

**Input:** media file, player/embed URL, thumbnail URL, landing/watch page, transcript/captions, duration/upload date, rights and hosting restrictions.
1. Distinguish these URLs explicitly; embedUrl is a player, contentUrl the actual video resource, watch page the HTML destination. Do not swap them in markup.[12]
2. Decide whether watching this video is the page's main purpose. A supplemental product/blog clip is not a dedicated watch page; do not guarantee video features just because VideoObject validates.[12]
3. Check indexable accessible watch page, prominent playable video, no mandatory interaction to reveal the only video, stable thumbnail/file access, supported media type. Test mobile, captions, poster and playback errors.
4. Human-check transcript/captions, speaker attribution, timing, important on-screen information and accessibility. Do not hallucinate content from title/thumbnail; use `process_video` when transcription is needed.
5. Draft accurate VideoObject only against current required/recommended properties. Consider video sitemap with current official schema, not stale template fields. Hosting/platform restrictions may limit fetching; document rather than bypass.
6. For third-party embedded video, both host and your valid watch page may appear; do not promise yours will be selected.[12]
**Output/validation:** URL-role mapping, technical/rights/accessibility findings, structured-data/sitemap draft. Test rendered playback, resource statuses and rich-result validation; then actual video indexing/report evidence. Views on a host ≠ referrals/conversions on your site.

## C. News

**Input:** actual publication/newsroom, original reporting, authors/editorial/contact policies, dates/timezone, article URLs, rights, corrections and sponsorship policy.
1. Qualify news value; a generic commercial landing page does not become news via NewsArticle markup.
2. Verify primary evidence, bylines, real publication/update dates, author/publisher identity and contact details. News policy emphasizes transparency; sponsored material must be disclosed.[23]
3. Keep article URL stable, accessible, canonical and crawlably linked; mark substantive updates honestly, not fresh dates to game recency. Article markup must describe the actual article and current supported feature.
4. Draft/validate News sitemap only if appropriate. Official guidance: include articles created in the last two days; remove older URLs or their news metadata from that sitemap, not the useful article itself. Up to 1,000 news entries per sitemap; split when necessary. Preserve original publication date/time and correct publication/language/title.[14]
5. Re-check current News policies and product enrollment/discovery rules before claiming a UI signup/submission is required or sufficient. Do not promise acceptance from a sitemap or Publisher Center presence.
**Output/validation:** editorial-transparency gaps, eligible recent URL set, validated sitemap DRAFT and cadence/owner. Count eligible timestamps/entries in code. After authorized changes verify public sitemap and article facts; measure News surfaces separately from ordinary web traffic.

## D. Discover

**Input:** indexed useful pages, audience interests, representative licensed imagery and available Discover report.
1. Confirm useful original content and compliance with current content policies; avoid clickbait, sensational hidden information and false previews.
2. Google says no special tags/schema are required; indexed compliant content is eligible, but eligibility is not guaranteed appearance.[13]
3. Inspect large representative preview images and permissions. Current guidance recommends at least 1200 px width and `max-image-preview:large` (or another supported route); verify current specs/aspect and actual crop before changing. Not a guarantee or universal image SEO minimum.[13]
4. Check consistent og/image or supported primary-image metadata, clear headline and author/date when appropriate. Do not fabricate freshness or force a News label.
5. Review report availability/threshold and date range via real authorized access; absence of a report ≠ measured zero. Report actual impressions/clicks/CTR where available, never invented Discover rank.
**Output/validation:** eligibility/preview audit, factual DRAFT changes and supplemental-traffic experiment. After approval test live image/robots metadata; compare cohorts and periods cautiously. Google explicitly describes Discover traffic as less predictable than keyword search; do not budget on guaranteed recurrent delivery.[13]

## Cross-surface completion

For each asset list `rights`, `accessible`, `markup valid`, `eligible`, `observed`, `traffic`, `conversion` separately. Technical pass does not prove the next status. Include excluded assets, access gaps, next owner/date and rollout/rollback.
For ecommerce/multilingual/local media combine relevant modules; for AI citations use `aieo-visibility`, not a media eligibility score.

## Evidence

Image docs [11], video docs [12], Discover [13], News sitemap [14], News policy [23]. Revalidate current detailed feature/sitemap schemas before implementation. Sources: [sources.md](sources.md).
