# GA4 data-quality checks before insights

Use this list when a country/channel report looks commercially implausible.

## Red flags

- `Unassigned` or `(not set)` accounts for a material share of sessions or revenue.
- One country dominates the whole property without a matching known business rationale.
- Very high sessions per active user in a channel or source.
- Revenue is concentrated in `Unassigned`, while recognizable acquisition channels report almost none.
- Revenue has the opposite sign from the business convention or jumps sharply without an operational explanation.

## Interpretation discipline

1. Separate **traffic direction** (users/sessions moving up or down) from **commercial attribution** (which channel generated revenue).
2. Do not call a channel profitable when source/medium is missing or most revenue is unattributed.
3. If the project asks to invert negative GA4 financial values, label the output as an explicit display convention and retain the raw sign in a raw export if available.
4. Investigate GA4 events and tagging before recommending spend shifts: purchase/refund events, server-side events, UTM persistence, cross-domain rules, bot filtering, and referral exclusions.

## Minimum insight output

- global monthly movement;
- country concentration and the largest growing/declining countries;
- acquisition-channel mix;
- one clear data-quality warning when attribution is unreliable;
- a prioritized next technical validation step.
