# Центральный Topvisor: безопасные границы

Рабочий каталог `${SEO_TRACKER_DIR}`, descriptor `projects/<id>.json`, shared credentials только центральный git-ignored `.env` / environment. Не раскрывать и не копировать секреты. Сначала читать текущий README и реально вызываемые scripts; документация может отставать.

## Примеры host-specific точек входа (не включены в пакет)

Это контракт ранее рассмотренной внешней реализации, не обещание наличия этих файлов/API у нового оператора. `${SEO_TRACKER_DIR}` задаётся только для уже разрешённого совместимого сервиса. Если файлов нет или интерфейс отличается — discovery/read-only adapter либо blocker; не создавать фиктивные scripts и не устанавливать сервис автоматически.
- `node scripts/check-project.mjs <id> --validate-only` — validation descriptor, не сбор позиций.
- `node scripts/run-topvisor-checker.mjs <id>` — price-only: `get/positions_2/checker_price`; не paid check. Использовать для non-secret price/limit preview после чтения актуальной реализации.
- `node scripts/run-topvisor-checker.mjs <id> --execute --wait` — paid checker; только после согласия на точный scope и цену. `--wait` не даёт права повторно запускать платную проверку.
- Для чистых read-only diagnostics использовать подтверждённые `getProjects`, `getKeywords`, `getHistory` из `scripts/providers/topvisor.mjs` через небольшой контролируемый runner; не угадывать их сигнатуры. Не печатать raw account data.

## Обязательная проверка реализации
1. Скрипт checker может завершиться по условию `cells > 0 && stable >= 2`, даже если `expectedCells` больше. Поэтому **не доверять exit 0**: независимо сверить exact matrix/дату/регионы/keywords и pending cells. Stable shortfall = incomplete, не падение позиций.
2. `scripts/weekly-check.mjs` может вызывать `ensureSitemapSubmitted()` раньше ветки `dryRun`. Функция в `scripts/submit-sitemap.mjs` использует PUT, если sitemap ещё нет. Поэтому `check-project --dry-run` **не является гарантированно read-only**. Не запускать как безопасный probe. `--no-telegram`/`--no-slack` выключают доставку, не sitemap write.
3. Общий runner может сохранять snapshot и отправлять уведомления. Согласие на paid positions не означает согласия на sitemap submission или нового адресата.
4. При обнаружении этих проблем зафиксировать blocker и предложить отдельную scoped доработку tracker. Не исправлять сервис/учётные данные/cron/сервисы в ответ на ошибку проверки.

## Согласованный recurring поток
Price и согласованный предел → ровно один paid job → статус existing job/завершение → полная проверенная history → сохранение без перезаписи старого snapshot → отчёт → разрешённая доставка. Для timeout сохранить job/date/context и проверить его состояние, а не повторять charge.

Отчёт: rank source, paid-check status, реальные baseline/current dates, key/region/device counts, expected/observed cells, non-secret cost+currency, completeness, raw/derived artifact paths. Если credentials/access не работают — назвать ошибку, не подставлять GSC или старую историю. Гарантированные суммы и `has_more` нужно сверить кодом.
