# Organic и AI: связь с бизнес-результатами

1. Проверить реальный GA4 property/account, доступные dimensions/metrics через discovery/metadata и совместимость запроса. Отсутствие инструмента в текущем чате не доказывает отсутствие интеграции; использовать существующий разрешённый Google workflow, не выдумывать MCP.
2. Согласовать ключевое событие: реальная успешно завершённая заявка/регистрация/покупка, не любой click. Проверить instrumentation, consent, duplicate events, filters/internal traffic. Не отправлять тестовую настоящую заявку без согласия.
3. Срезы: landing page + query string normalization rules, session source/medium/channel, country/device, полные интервалы и timezone property. Source user-first и session-source не смешивать. Query strings могут содержать PII, очистить перед артефактами.
4. AI referrals выделять по наблюдаемым referrer/source domains, сохранять allowlist и дату. Не присваивать Direct/Unassigned к AI и не считать API-ответы трафиком. Не обещать полный охват AI-переходов.
5. Organic conversion: числитель/знаменатель определены в одном scope. Сессии с key event / eligible sessions — conversion rate; число key events / sessions — другой показатель. Метрики API и UI проверить, не угадывать имя поля.
6. CRM match использовать только по разрешённым обезличенным ID, с одним определением qualified lead и maturity окна. GSC query-level данные нельзя связать с конкретным человеком в GA4. Aggregate page/date correlation не attribution.
7. Выручка GA4 — аналитический сигнал; оплаченные outcomes и возвраты сверять с разрешённой системой учёта. Валюты не суммировать, знаки не менять без явного указания пользователя.
8. Сохранить ограниченные raw/derived exports, metadata/row counts/filters, sampling/threshold/data-loss warnings. Если эти показатели интеграция не раскрывает — статус unknown, не 'несэмплированные полные данные'.

Выход: cohort table + metric definitions + качество данных + business interpretation + next measurement. Это не автоматическая публикация Google Sheets и не доказательство причинного эффекта SEO.
