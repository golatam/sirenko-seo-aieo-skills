# Яндекс / Вебмастер / Алиса AI

## Input → output → validation

**Input:** домен/host и права, страны/языки/регионы, бизнес-модель, страницы/фиды, разрешённые выгрузки Вебмастера/Метрики и AI-наблюдения.
**Output:** [yandex-evidence.md](../templates/yandex-evidence.md), capability matrix, technical/content findings, URL/region/feed backlog, scoped Alice visibility baseline и тест.
**Validation:** сначала текущая официальная документация и реальный read; UI/export/API не смешаны, метрики имеют точный scope/знаменатель. Ни ИКС, ни валидная schema не гарантия позиций/Алисы.

## 1. Discovery — не выдумывать интеграцию

1. Начни с официальной справки Вебмастера и обзора ресурсов API.[15] Зафиксируй version/date, auth/scopes, owner, target host, квоты и семантику нужного метода.
2. Через доступный tool catalog проверь фактические схемы/permissions. Наличие официального API не означает существующий MCP или авторизацию в этой сессии.
3. Выполни только разрешённый безопасный sample read (или используй пользовательский экспорт). Запиши request/filter/date range/response fields, pagination/total/coverage. Не выдумывай команды/API paths по аналогии с Google.
4. Матрица `capability → official doc → UI/export/API → actual tool → authorized? → sample read → gaps`. POST может быть read-query или изменением — классифицировать по документации, не только HTTP verb.
5. Нет API/авторизации — ручной export из конкретного экрана с filters/date/properties, не обещание автоматического мониторинга.
Все hosts/verification/recrawl/feed/sitemap/settings submissions — отдельные внешние действия с preview, confirmation и exact read-back; никаких токенов в артефактах.

## 2. Яндекс Search baseline и технический разбор

Выбери нужные официально описанные ресурсы: site summary, diagnostics, indexing samples/history, query reports, external link samples и feeds, если они доступны аккаунту.[15] Summary count и samples не полный список; проверить pagination/definition до агрегирования.
Построй URL inventory: status/redirect, canonical и главный адрес, robots/indexability, sitemap, доступность контента и дубли. Для Yandex-specific директив/region controls/JS rendering сначала читать актуальную справку; не переносить Google правила автоматически.
Сопоставь исключённые/ошибочные страницы с реальным fetch/render и diagnostic reason. Robots disallow не становится подтверждённым удалением из поиска. Recrawl request не гарантия индексации.
Отдельно проверь региональные данные/контакты и фактическую географию бизнеса. Если нужен Яндекс Бизнес, сначала найти текущие официальные eligibility/rules и read-only состояние карточки; не создавать fake offices и не угадывать supported API.
Для магазина discover актуальные Яндекс feed/YML/category/merchant требования и сверить товарные IDs, варианты, stock/price, доставка. Это отдельный target contract, не Google feed с переименованным заголовком. Без прочитанных требований — `research required`, не готовый upload.

## 3. Алиса: что подтверждено и как читать

Официальная справка описывает источники в ответах Алисы, возможность ответа без ссылок и изменение ответа/источников со временем/персонализацией.[19] Порядок citations не выдавать за органический rank.
Проверенная документация описывает UI-инструмент «Видимость сайта в Алисе AI» в Вебмастере: последние 3 месяца, еженедельное обновление, ограничение запросами, где сайт уже достаточно высоко в поиске; SoV, примеры сайтов, запросов/страниц и скачивание списка запросов.[20]
Это **документированная возможность UI**, не подтверждённый доступ к аккаунту или API. В проверенном обзоре ресурсов [15] отдельный Alice endpoint не установлен; это не доказательство, что его нигде нет. Перед автоматизацией повторно discover текущий метод/схему/auth и sample read.

При доступе:
1. Открыть exact property и экран, зафиксировать filters/period/update date и `insufficient data` state.
2. Сохранить scoped export/query sample с исходными заголовками; не реконструировать недоступные значения из графика.
3. SoV — доля запросов с упоминанием сайта в ответах Алисы относительно запросов с ответами в покрываемой инструментом выборке; не доля всего рынка, не impression/click share.[20]
4. «Примеры» — выборка и произвольный порядок; не полный universe, не рейтинг конкурентов. Отсутствие top notification не означает zero citations.
5. Статистика не click/impression report; referrals/конверсии получать отдельно из разрешённой analytics. SoV нельзя сравнивать напрямую с другим вендором/ручным prompt panel.[20]

## 4. Manual observed-answer panel

Согласуй целевые intents и рынок; фиксируй query verbatim, language, engine/surface (Поиск с Алисой vs отдельный chat), date/time, device/account/personalization context, repeated run ID и response evidence.
Классифицируй `answer not shown`, `answer without sources`, `sources shown no target`, `target cited`, `inaccessible`; это разные состояния, не все «ноль».
Для citation сохрани exact source URL, response excerpt, page excerpt, язык/рынок страницы и fidelity (подтверждает ли источник claim). Соседняя ссылка не означает, что она подтверждает всё предложение.
Повторы/парафразы/разные даты нужны для устойчивости; конкретный размер панели зависит от ресурса и цели, не «магическое число». Метод в `aieo-visibility`. Масштабный сбор только разрешённым инструментом/каналом с утверждённой стоимостью.

## 5. Из наблюдения в работу

- Не в поиске/технически недоступно → `technical-seo-audits` + Яндекс-specific проверка.
- Неверный рынок/локальная версия → international/local module, real presence gate.
- Страница не закрывает intent/устарела → `seo-content-operations`, проверенные источники, экспертиза/оригинальные данные.
- Соседний publisher полезно покрывает тему → qualified prospect в `seo-authority-promotion`, не покупка ссылок/цитат.
- Ошибка AI ответа → evidence-backed correction DRAFT; feedback submission после confirmation, без обещания изменить модель.

## 6. Pilot и измерение

Зафиксируй гипотезу и baseline; small cohort + comparable control, если допустимо. Перед изменением exact URLs/fields, reviewer/approval, risk/rollback. После — read-back факта публикации, затем отдельно проверка Search/Alice наблюдений.
Сравни query/page/indexing performance, UI SoV (его scope), panel citations и реальные referrals раздельно. Укажи недели обновления, неполноту, сезонность/параллельные изменения. Даже рост SoV после правки не доказывает причинный эффект правки.
Итог: verified facts / hypotheses / unknown / unsupported integrations, следующий owner/date. Ни наличие навыка, ни найденная документация не означают подключённый Вебмастер.

## Evidence

API resource discovery [15], механизм ответов [19], UI visibility/report limits [20]. Полные ссылки/дата: [sources.md](sources.md).
