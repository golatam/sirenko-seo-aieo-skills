# Измерение и эксперименты

## Проверка данных до интерпретации
1. Для каждого источника получить latest available date, период, timezone, фильтры, rows/total/has_more. Финальные и preliminary данные не смешивать.
2. Сверить точную матрицу ranks (keyword ID × engine × region × device × date), AI panel version и URL cohort. Сравнивать matched universe; новые/удалённые показывать отдельно. Нераспознанный engine нельзя автоматически считать Google.
3. Проверить tracking changes, consent, redirects, campaign tagging, bots, internal traffic и события-дубли. В данных с lag сначала восстановить measurement, не ставить SEO-диагноз.
4. Считать изменения программно: absolute=current−baseline; relative=(current−baseline)/baseline только при baseline≠0. При нулевой базе выводить абсолютное изменение и 'relative undefined', не бесконечный рост.

## Воронка
Impressions → clicks → landing sessions → meaningful key event → qualified lead → confirmed outcome. Это связанные, но не тождественные выборки и не всегда объединяемые пользователи. GSC не предоставляет индивидуальный join к GA4. Сравнение по page/period/segment не является person-level attribution.

- CTR = сумма clicks / сумма impressions при совместимой агрегации. Page/query суммы GSC могут расходиться с totals из-за анонимизации/фильтров.
- Session conversion rate = sessions with specified event / eligible sessions, не event count/sessions без определения. Если доступно только число событий, назвать event-per-session rate.
- Lead quality rate = qualified leads / captured leads с одинаковой датировкой и maturity.
- Выручка отдельно по валютам и подтверждённой системе учёта. Нельзя автоматически исправлять знаки, конвертировать валюты или называть GA4 revenue прибылью.
- AI referrals — наблюдаемые source/referrer, не все визиты из ИИ. Direct/unknown не перераспределять догадкой.

## Диагностика
| Наблюдение | Следующая проверка |
|---|---|
| Все источники одновременно обнулились | Авторизация/сборщик/фильтр/истечение доступов |
| Impressions↓, positions stable | Спрос/сезон/состав тем/география, полнота GSC |
| Position↓ в важных matched segments | Index state, релиз, конкуренты, официальные обновления |
| Impressions stable, CTR↓ | SERP features/snippet/device mix, не только переписать title |
| Clicks stable, sessions↓ | Consent/tracking/redirect/referral/session definition |
| Sessions stable, qualified leads↓ | CTA/формы/качество intent/операционный учёт |
| AI citation↓ один день | Повторные замеры, surface/model/search-mode/panel drift |

## Протокол теста
До изменения зафиксировать: hypothesis, target pages, market, primary metric, guardrails, baseline window, matched control, минимальный practically meaningful effect, ограничения данных, длительность/правило остановки, расходы и ответственного. Не выбирать победителя постфактум по лучшему из десятков показателей.

Если трафик достаточен: сопоставимые page clusters/control, baseline trends, раздельный анализ устройств/стран, стабильная instrumentation. Не смешивать большой редизайн, миграцию и контентную правку, если требуется понять механизм.
Если трафик мал: ограниченный пилот, повторные наблюдения, qualitative evidence; не имитировать статистическую значимость. AI repeats внутри одной prompt-family/date не считать независимыми людьми/запросами. Доверительные интервалы и resampling строить по корректной единице наблюдения; модель CI назвать.

Статусы: supported / not supported / inconclusive. Рост после изменения сам по себе — correlation. Не предписывать универсальное число повторов или дней; оно зависит от шума, эффекта, покрытия и бюджета.

## Мониторинг и доставка
Согласовать threshold, minimum absolute volume, persistence window, recipients, cooldown, recovery alert, per-run/per-month budget и стоп при failure. Для нормы — тихий режим, для новой ошибки/восстановления — короткое сообщение в разрешённое место. Существующее согласие на конкретный cron не разрешает подключить новые платные endpoints или публиковать новый отчёт.
