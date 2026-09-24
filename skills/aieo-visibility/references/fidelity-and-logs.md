# Manual citation fidelity and bot-log protocol

## Citation fidelity: claim → cited source → support

1. Preserve the actual answer, model/surface/mode/time and original clickable citation target/marker. Capture full context; a search result snippet or analyst paraphrase cannot substitute for the source or answer.
2. Split the cited passage into atomic claims. For each claim–citation pair save exact answer quote, target URL, resolved final URL, HTTP/access result, capture timestamp, source artifact/version/hash, exact source quote with surrounding context, locale and coder ID. Hash with a tool; never invent archived versions. If judging 'as of answer date' but only today's source exists, label temporal uncertainty.
3. Assign one label:
   - `supported`: source explicitly substantiates the full claim, including quantities, scope, conditions and date.
   - `partial`: supports part only, or qualifiers materially differ.
   - `unsupported`: inspected accessible source fails to substantiate or contradicts the claim. Explain the missing claim, not just 'URL works'.
   - `unverifiable`: source inaccessible/paywalled/changed, ambiguous citation mapping or historical evidence missing.
   - `not_reviewed`: pair captured but no fidelity inspection yet.
4. Keep source identity/relevance, quotation accuracy, factual truth and source authority as distinct checks. A faithful citation can accurately repeat a false source. Invoke `claim-verification` for truth; a linked domain isn't proof. Do not mark an accessible URL 'supported' automatically.
5. Review all high-risk business claims (price, regulation, capabilities, geography, eligibility) and a predefined stratified sample of other pairs. Keep reviewed/all-pair coverage. Use a second human/agent reviewer for a subset, retain disagreements and adjudication; do not make agreement look like independent source evidence.
6. Output examples, label counts, fully supported/reviewed ratio and coverage. Exclude unverifiable/not-reviewed from fidelity denominator but disclose them. A missing source is unknown, not unsupported by default. The local script trusts labels/evidence locators; it neither fetches sources nor verifies source_quote mechanically.

## Bot logs: access evidence, not AI visibility

Use approved CDN/WAF/origin log exports, scoped dates/domains and minimum required fields. No new logging service or external upload of production logs by default. Avoid storing cookies, authorization headers, query-string PII or full client IPs in published reports.

1. Record log source, timezone, export/query filters, retention gaps, sampling/drop rules, cache/origin coverage and bot-verification capability. CDN served/cache hits may not reach origin; an origin-only absence does not prove no visit.
2. Preserve request ID, timestamp, hostname/path (PII-redacted), method, status, UA, bytes/latency, cache status, WAF action and bot verification evidence in a private artifact. Deduplicate by provider request/event ID plus documented key; never collapse legitimate retries just because UA/path/time resemble each other.
3. Classify declared UAs independently of verification: search retrieval / training-related / user-triggered / unknown. A UA string is spoofable. Use official published IP ranges or provider-documented reverse+forward DNS method where applicable, saving verification result, source URL and retrieval date. Unverified-UA counts remain separate; don't apply a Google verification method to every provider.
4. Official OpenAI roles (https://developers.openai.com/api/docs/bots): **OAI-SearchBot** surfaces sites in ChatGPT search; **GPTBot** crawls content that may be used for model training; controls are independent. **ChatGPT-User** performs user-triggered actions, not automatic crawling/search eligibility, and robots rules may not apply. One allowed crawl may be reused for both search/training use cases when both allowed, so a request isn't proof of training. Published range links are provided by that page; fetch current ranges only in a separately authorized log-verification task.
5. For Bingbot/Googlebot/ClaudeBot/PerplexityBot and other agents, verify current official names, roles and identity procedures before labeling. A bot name that 'sounds AI' isn't evidence. Google Search generative inclusion is a separate Search Console control; Google-Extended concerns training, not a replacement for Search visibility controls.
6. Summarize by verified bot category/domain/path group/date: requests, unique URLs, 2xx/3xx/4xx/5xx, 429/403, WAF challenges, latency and cache ratio. Report status unknown/missing fields and known export gaps. Count a robots.txt request separately from content fetches; 200 alone doesn't prove useful content (challenge pages can be 200).
7. Diagnose concrete access failures with URL/time/status/log evidence and route a proposed fix to `technical-seo-audits`. Never auto-allow all bots, disable WAF globally or publish robots edits. Get scoped approval, test a small rule, then verify with independent requests/log readback.

## Triangulation and honest conclusions

A verified bot hit proves a request, not indexation, training, retrieval selection, answer citation or a human session. A robots allow rule proves policy, not a hit. Absence under sampling/cache/retention gaps is not a universal negative. Align log windows with actual response and native console timestamps before suggesting a hypothesis; correlation is not causality. AI referrals/conversions require a separate analytics attribution model; missing referrer, app redirects, consent and self-referrals limit coverage. Never turn crawl volume into a GEO score.
