---
name: seo-reporting-monitoring
description: "Use when measuring SEO/AIEO results and regressions."
version: 2.0.0
author: Sirenko SEO/AIEO Skills contributors
license: MIT
created_by: agent
metadata:
  seo:
    tags: [seo, aieo, monitoring, measurement, experiments]
    related_skills: [seo-aieo, rank-tracker-operations, google-search-console-operations, ga4-project-reporting, aieo-visibility, seo-content-operations]
---

# SEO/AIEO: результаты, отклонения, следующий цикл

## When to Use
Для исходного измерения, регулярного отчёта, падений видимости/трафика, проверки эффекта внедрения, content decay, экспериментов и очереди обновлений. Позиции собирать через `rank-tracker-operations`, GSC через `google-search-console-operations`, AI-наблюдения через `aieo-visibility`.

## Procedure
1. Прочитать descriptor/brief, предыдущий отчёт, цель, журнал релизов, manifest источников и согласованное расписание. Подтвердить точные account/property/domain/markets/languages/devices.
2. Определить текущий и базовый **полные** интервалы. Использовать последнее доступное полное окно, а не автоматически вчера; показать фактические даты, timezone и задержку каждого источника. Сезонность/год-к-году отдельно. Старый baseline не называть weekly.
3. Выполнить запросы нужных источников, сохранить evidence и coverage. Проверить пагинацию, totals, завершение paid jobs, панель ключей/промптов, сбои аналитики, consent и потерю attribution. Недостающие источники показать отдельно, не заполнять нулями.
4. Считать в коде независимые блоки:
   - **SERP**: Topvisor позиции и изменение по совпадающим keyword/engine/region/device; known OUT отдельно от pending/missing/error.
   - **Search traffic**: GSC clicks/impressions/CTR/average position с caveats, brand/nonbrand, pages, queries, countries/devices, Google/Yandex отдельно.
   - **AI**: native-console показатели и повторные ответы панелей по отдельной методике; mention/citation/fidelity не смешивать с positions. Google AI impressions, Bing Citation Share и Яндекс/Алиса SoV имеют разные знаменатели; методика и доступность — в `aieo-visibility`, не складывать их в общий индекс.
   - **Сайт**: indexability и измеренное index state, template regressions, HTTP/links/schema/CWV, fresh/stale content.
   - **Бизнес**: organic landing cohorts, key events, качественные заявки и подтверждённые продажи из разрешённой системы учёта. Не считать GA4 финансовым реестром.
5. Разложить изменение по причинам: data loss → спрос/сезон → состав запросов → позиции → CTR → посадочные → conversion. Совпадение дат с релизом/апдейтом не доказывает причинность. Методика: `references/measurement-and-experiments.md`.
6. Для отклонения задать URL/segment, baseline/current, величину и предел шума, evidence, предполагаемую причину, уверенность, владельца и next action. Общий «SEO score упал» недостаточен.
7. Сформировать очередь: fix / update / consolidate / investigate / experiment / no action. На удаления, redirect, публикацию и outreach нужны подтверждения. У каждой работы критерий проверки и повторный замер.
8. Записать отчёт через `templates/report.md`. При внешней доставке проверить адресата и утверждённый scope; не создавать cron/таблицы/публикации автоматически.

## Topvisor: обязательная граница
Если `rankSource: topvisor`, реальный вызов Topvisor обязателен. GSC/Yandex average position и публичная выдача его не заменяют.
- Внешний центральный tracker (не входит в пакет): `${SEO_TRACKER_DIR}`; пример descriptor `projects/<id>.json`. Сначала подтвердить совместимость реального host-сервиса; при его отсутствии — blocker, не выдумывать bundled CLI.
- Перед manual paid run: price/counters/regions/keywords → явное подтверждение → запуск. Согласованная recurring задача действует только внутри своего бюджета, проекта и расписания.
- В отчёте: paid-check status, history date, region/key counts, expected/observed cells, non-secret price/counters, snapshot/report paths.
- Exit 0 от checker не является доказательством полноты. Сверять expected matrix; при shortfall маркировать incomplete и не выпускать отчёт о падении позиций.
- Сначала читать `references/topvisor-central-tracker-cron.md`: общий runner может иметь внешние действия даже при dry-run. Авторизация/кодовые ошибки не повод ремонтировать инфраструктуру.

## Pitfalls
- CTR по строкам нельзя усреднять арифметически: считать clicks/impressions при совместимой агрегации.
- Меняющийся keyword/prompt set разрушает сравнение; показывать matched panel и добавленные/удалённые элементы отдельно.
- Не делать OUT=101 без оговорённого определения/глубины; не подменять пропуски позицией.
- Error/no-search/нет данных в AI — отдельные состояния; локальный score не доказывает цитирование.
- Нельзя присвоить органике `Unassigned` или AI весь Direct; referrer — неполное наблюдение.
- «Внедрено» ≠ «проиндексировано» ≠ «выросло». При недостатке наблюдений итог эксперимента — inconclusive.

## Verification
- Источники реально запрошены, даты/охват/полнота проверены или блокер явно назван.
- Метрики вычислены из сохранённых данных, сравниваются одинаковые группы и полные периоды.
- Отчёт включает business outcome, приоритетную очередь и неизвестное, а не только графики.
- Настройки мониторинга, paid checks и внешняя доставка не расширены без согласия.
