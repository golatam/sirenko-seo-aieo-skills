# Provenance and evidence — promotion

Checked: 2026-09-24. These are references for decisions, not performance guarantees. Before an external action re-read current policies and actual tool schemas. Workflow text is original; no donor scripts, dependencies, installer, API credentials or external writes imported.

## Adoption decisions

AgriciDaniel/claude-seo `skills/seo-backlinks/SKILL.md`, commit `e77e783e38eeb738424eb72117abbd2dacdd88af`: adopted source inventory, source sufficiency and actual link verification/JS uncertainty.[1]
Rejected universal anchor/follow/link-count thresholds, TLD quality labels, blended health scores and numerical vendor confidence, automated toxicity/disavow, and provider-specific setup claims. Public search is partial; metrics stay provider-specific.
Google spam policy supplies the no-manipulation boundary and qualification of paid links; it does not prove earned PR ROI.[5]
Google disavow guidance supplies the advanced-risk/manual-action gate; this workflow never automatically generates/uploads a disavow file.[16]
MIT was checked at the same donor commit; notice retained below.[4]

## Source/claim limitations

- Source files were retrieved and selected sections reviewed, not executed or production-audited.
- Official pages were read; material link-spam/disavow rules additionally checked in direct HTML text where extraction dropped lists.
- Private evidence snapshots, build reports and citation ledger are excluded from distribution and are not runtime dependencies. Public pinned references and license notice are below; see also the repository source register (`${SEO_PACK_ROOT}/SOURCES.md`, optional checkout documentation).
- No backlink provider account/API access was established; no client-site outcome was measured.

## Sources

[1] https://raw.githubusercontent.com/AgriciDaniel/claude-seo/e77e783e38eeb738424eb72117abbd2dacdd88af/skills/seo-backlinks/SKILL.md
[4] https://raw.githubusercontent.com/AgriciDaniel/claude-seo/e77e783e38eeb738424eb72117abbd2dacdd88af/LICENSE
[5] https://developers.google.com/search/docs/essentials/spam-policies
[16] https://support.google.com/webmasters/answer/2648487?hl=en

## Donor license notice

MIT License

Copyright (c) 2026 agricidaniel

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
