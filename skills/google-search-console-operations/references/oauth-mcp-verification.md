# GSC OAuth/MCP readiness and safe recovery

## Readiness evidence

1. Existing approved credentials expose the required read scope; inspect only scopes, expiry and presence of refresh capability, never token values.
2. MCP discovery/test returns the expected read-only tools.
3. `list_sites()` returns the exact target `siteUrl` and an adequate permission level; do not assume all users must be siteOwner to read.
4. A small real read for the selected report succeeds. Empty rows can be valid but do not establish data coverage. A stored token, docs page or listed tool alone is not proof of full access.

## Recovery without secret leakage

Read the documentation of the OAuth helper in use and, for remote OAuth, of the MCP server. Inspect the existing approved helper and its help/schema, including how it receives the callback. Never invent OAuth code exchange or client credentials. No passwords, client secrets, authorization codes, full redirects or refresh tokens in any chat or tool-output transcript; use the approved secure UI/callback/local input channel. If unavailable, stop with an authentication blocker rather than falling back to code-in-chat. Do not copy stale helper examples that solicit those secrets in DM.

Keep `webmasters.readonly`; widening/revoking/replacing shared Google scopes requires explicit approval. Check whether the credential supports durable refresh; distinguish refresh failure from insufficient scope, API disabled, wrong account/property or permission. Do not blanket-revoke Workspace credentials for a GSC error. Token/pending files should be `0600`, state+PKCE bound to one attempt and pending state removed by the helper. Do not set global insecure-transport flags or fabricate redirect ports.

## MCP/runtime boundary

Using an existing connector is not permission to modify its server or client config. Read schemas each session: wrapper defaults may differ from official API defaults. When a separately authorized integration task changes configuration, test before activation and prefer an operator-approved supported reload. **No automatic service restart**. A necessary restart is a separate approved infrastructure action, not an analytics step.

| Symptom | Safe check |
|---|---|
| Property missing | Account and exact property from `list_sites`; URL-prefix and sc-domain are distinct |
| Insufficient scope | Non-secret scope metadata and approved incremental authorization path; preserve other integrations |
| Tool not found | Schema/discovery/runtime status; report blocked capability, do not invent a tool |
| Module/import error | Approved integration interpreter/dependencies; no installation as side effect of reporting |
| Fresh or empty report | Finalized dates, filters, report availability, low-data threshold; AI inclusion setting read-only |
| Reauthorization required | Protected UI/helper callback or stop; never solicit code/redirect in chat |
