---
name: google-search-console-operations
description: "Use when operating Search Console. Verify access and totals."
version: 2.0.0
author: Sirenko SEO/AIEO Skills contributors
license: MIT
created_by: agent
metadata:
  seo:
    tags: [gsc, search-console, oauth, analytics]
    related_skills: [aieo-visibility, google-workspace, remote-mcp-oauth-operations]
---

# Google Search Console: подключение и работа

## When to Use

Используй для подключения GSC к Hermes, проверки прав на сайт и получения данных по поисковому трафику, запросам, страницам и sitemap.

## Принципы

- Для постоянной работы агента предпочитай **OAuth пользователя** с областью `https://www.googleapis.com/auth/webmasters.readonly`: он не требует отдельного сервисного аккаунта и отражает реальные права владельца сайта.
- Интеграция должна быть read-only, если пользователь явно не просит иное.
- `site_url` должен совпадать с именем свойства в GSC: для domain property обычно `sc-domain:example.com`, для URL-prefix — полный URL с протоколом.
- До любых выводов о сайте сначала запроси список доступных свойств и подтверди, что нужное свойство есть в нём.

## OAuth-подключение

1. Сначала используй уже подключённый read-only MCP: загрузи актуальные схемы, вызови `list_sites`, выбери точный `siteUrl` и проверь read-only запросом нужный отчёт. Не запрашивай новый OAuth без причины.
2. Если авторизация отсутствует/истекла, загрузи `hermes-agent`, `google-workspace` и, для удалённого OAuth MCP, `remote-mcp-oauth-operations`. Найди уже одобренный helper и проверь его `--help`, поддержку нужного scope и безопасного callback; не изобретай собственный обмен кода, localhost-port-1 flow или глобальное отключение TLS/OAuth-проверок.
3. Покажи владельцу аккаунт/проект, цель, запрашиваемые права и ограничения. Предпочитай `https://www.googleapis.com/auth/webmasters.readonly`; не отзывай и не перезаписывай общий Google token, не меняй существующие scopes без согласования. Обновление должно сохранять только ранее одобренные необходимые области, а не запрашивать весь Workspace автоматически.
4. Не проси пароль, client secret, authorization code, полный redirect URL, access/refresh token **ни в каком чате**, включая личный. Используй защищённый OAuth UI/callback существующего helper или ввод пользователем непосредственно в одобренный локальный процесс без попадания секрета в разговор/командную строку. Если такого пути нет — остановись с блокером безопасной авторизации. Это ограничение имеет приоритет над устаревшими примерами пересылки code/redirect в смежных skills.
5. Проверяй только не-секретные метаданные (scopes, срок действия, наличие refresh token, права файла), никогда значения. Helper должен проверять state/PKCE и связывать callback с одной попыткой; token/pending files — `0600`, pending удаляется после завершения. Не добавляй секреты в SKILL/config/отчёт.
6. После авторизации — discovery и `list_sites`, затем реальный минимальный read-only запрос к точному property. Наличие token-файла не доказывает доступ или автоматическое продление. Проверку refresh и подключения выполняй только в согласованном scope, без перезапуска рабочего gateway.

## MCP-интеграция

Предпочитай существующий MCP в активном профиле. Добавление/изменение server/config — отдельная согласованная задача, не побочный эффект аналитики. Минимальный набор read-only tools:

- `list_sites()` — доступные GSC properties и уровень прав;
- `search_analytics(site_url, start_date, end_date, dimensions, ...)` — Search Analytics;
- `sitemaps_list(site_url)` — отправленные sitemap.

Сервер должен:

1. Использовать утверждённый backend credentials активного профиля; в существующей локальной реализации путь может задаваться `GOOGLE_TOKEN_PATH`, но не навязывай это удалённому MCP.
2. Использовать только одобренные read scopes; наличие широкой старой авторизации не разрешает изменяющие операции.
3. Поддерживать обновление credentials безопасным helper/provider flow с сохранением защищённых прав доступа; не выводить секреты.
4. Для локальной Python-реализации использовать уже настроенный interpreter с необходимыми Google/MCP зависимостями. Не устанавливать их как побочный эффект аналитики.
5. Проверяться двумя уровнями: `hermes mcp test <name>` и реальным `list_sites()` с проверкой нужного свойства.
6. Не перезапускать gateway автоматически. После отдельно согласованной конфигурации — проверить auth/discovery; активацию через поддерживаемый `/reload-mcp` согласовать с оператором. Перезапуск допускается только как отдельное явно подтверждённое действие, если reload недостаточен.

## Быстрые проверки

```bash
# Конфигурация и обнаружение инструментов
hermes mcp list
hermes mcp test gsc

# Логическая проверка API
# Ожидается среди результатов точное имя нужного property.
```

См. `references/oauth-mcp-verification.md` для проверенного сценария и типовых ловушек.

## Аналитика: воспроизводимость и ограничения

- Даты `YYYY-MM-DD`, границы включительные, дневной GSC — Pacific Time, не местный часовой пояс проекта. Сохраняй property, даты, search type, dimensions в порядке запроса, filters, aggregation, дату выгрузки и состояние свежести. Не смешивай неполные и финальные дни.
- Сначала запроси контрольные totals без `page`/`query` и с теми же остальными фильтрами/aggregation; затем детализацию. Для исследования спроса полезны `query` + `page`, но GSC — только наблюдаемые запросы сайта, не объём спроса всего рынка и не rank tracker. См. `references/search-analytics-accounting.md`.
- Пагинация: проверь текущую схему MCP. На проверенном `mcp__gsc__search_analytics` есть `row_limit` (default 100), `start_row` (default 0), `search_type` (default web), `dimension_filter_groups`, `aggregation_type`; нет exposed `dataState`. Передавай поля явно; не выдумывай отсутствующий параметр. Если другая обёртка не поддерживает offset, сообщи о частичной выгрузке или используй заранее одобренный API helper/UI export.
- Официальный API: `rowLimit` 1–25000, `startRow` с нуля; для больших выгрузок делай дневные запросы и увеличивай offset, сохраняя остальные поля. Остановись на короткой/пустой странице, проверяй повтор страниц и дубликаты ключей. Предел предоставляемых данных — 50K строк/день/search type, а не обещание всех запросов; учитывай privacy omissions и top-row limits.
- Не суммируй пересекающиеся выгрузки и разные aggregation types. CTR пересчитывай как clicks/impressions; position взвешивай по impressions только для совместимых непересекающихся строк, не усредняй средние и не называй это позицией rank tracker. Query/page-detail не восстанавливает скрытые данные totals.
- UI Search Generative AI report существует: impressions с dimensions Pages/Countries/Dates/Devices, отдельно Discover. Не путай с API Search Analytics: отдельный AI endpoint/type/filter в проверенной официальной схеме не подтверждён. Не изобретай `search_type=ai` или `AI_OVERVIEW` filter. Используй native UI export и `aieo-visibility` → `references/native-consoles.md`.
- Нулевой/отсутствующий AI отчёт не доказывает отсутствие AI-ссылок: проверь доступ, объём данных, даты, filters, а также Search generative AI control (включая наследование). Проверка read-only; изменение inclusion/exclusion требует отдельного согласия.
- Вывод: raw export + manifest + полнота/лимиты + проверяемые срезы + гипотезы. Наличие sitemap не доказывает индексацию, OAuth не доказывает доступ к каждому отчёту.
