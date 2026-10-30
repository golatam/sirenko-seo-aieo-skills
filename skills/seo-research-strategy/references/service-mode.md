# Service mode: topics file

Used when a service runs this skill unattended (see the Service mode section of SKILL.md). The output contract is `schemas/topics.schema.json` at the plugin root; if the plugin is installed without it, the summary below is the contract.

## Inputs

- `profile`: site profile YAML — `domain`, `language`, `markets`, `icp`, `product`, `competitors`, `brand_negatives`, `author`.
- `inputs`: whatever the service supplied, typically GSC and Yandex Webmaster query exports, the site's own URL list or sitemap, competitor sitemaps, SERP snapshots, and previously produced topics to avoid repeats. Treat missing inputs as missing, not as zero demand.
- Read-only public fetches (competitor sitemaps, SERP pages, documentation) are allowed. Paid provider calls are not: the service collects paid data itself and passes it in.

## Procedure

1. Keep each market lane from the profile separate; do not add up Yandex and Google numbers.
2. Build candidates from observed queries first (impressions without a matching page, positions 5–30, rising queries), then from gaps between competitor sitemaps and the site's URL list.
3. Drop candidates that an existing site URL already serves for the same intent, that duplicate an earlier topic, or that touch `brand_negatives`.
4. Group candidates into hubs. A hub has at most one `pillar`; the rest are `support` pages that link to it.
5. Score 0–100 as an integer priority, not a forecast: observed demand (up to 40), fit with `icp` and `product` (up to 30), gap versus site and competitors (up to 20), the author's ability to add real experience or sources (up to 10). State each contributing reason in `reasons`.
6. Every topic needs at least one `evidence` item pointing to the actual query, URL or export row. Fill `metric` only with an observed value and its period, e.g. `impressions 1200 / 28 days`. Never estimate volumes, difficulty or traffic.
7. Sort by score, highest first. Return fewer topics rather than padding with weak ones.

## Output fields

`{ site, generated_at, topics[], reasons? }`; each topic: `title`, `slug_hint` (a-z0-9-), `keywords[]`, `score` (0–100), `reasons[]`, `hub`, `role` (`pillar|support`), `intent` (`informational|commercial|transactional|navigational`), `evidence[]` of `{ type: gsc|yandex|sitemap|serp|other, ref, metric? }`. `site` is the bare domain; `generated_at` is ISO-8601 with timezone.

No usable evidence or no profile: write `"topics": []` and a non-empty top-level `reasons` naming what was missing (for example, `GSC export not provided`, `sitemap unreachable`).

Before finishing, parse the written file as JSON and check required fields, enums and ranges against the contract.
