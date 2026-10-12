# Earned promotion: asset → DRAFT → approval → verified outcome

## Контракт

**Input:** qualified prospects, inventory baseline, business goal, разрешённые данные, owner/reviewer, экспериментальный cap и сроки.
**Output:** asset/brief, DRAFTs, approval record, send log, placement evidence, measurement note.
**Validation:** полезность независимо от ссылки; claims воспроизводимы; права/approval подтверждены; send/live/conversion доказаны отдельно.
До старта согласуй decision rule и окно: продолжать при реальном editorial interest/qualified referrals, пересмотреть при систематическом отсутствии fit. Численные targets — проектная цель, не выдуманная отраслевая норма.

## 1. Asset по бизнес-модели

| Ниша | Полезный актив | Аудитория | Проверка |
|---|---|---|---|
| B2B/SaaS/pro services | Анонимизированный benchmark, calculator, integration guide | Отраслевая редакция, интегратор, ассоциация | Метод/выборка, consent, тесты; без обещаний ROI |
| Local/offline | Реальный районный справочник, данные о локальной проблеме | Местная пресса/сообщество | Настоящая география/данные; членство не endorsement |
| E-commerce/manufacturing | Спецификации, тест, compatibility/maintenance data | Buying/repair guides, профильная пресса | Реальные испытания, safety, stock/price; samples раскрывать, links не требовать |
| Publisher/education/nonprofit | Dataset, explainer, архив, карта | Журналисты, преподаватели, исследователи | Provenance/license; пресс-релиз не научное исследование |
| Regulated: finance/medical/legal/iGaming | Проверенный справочник или методика | Профильный эксперт/редакция | Country/domain review, permission, risk/age; никаких гарантий результата |
| International | Локальные данные и локализованный angle | Редакция рынка | Native reviewer, местные источники; не буквальный перевод нерелевантного benchmark |

Паттерны комбинируются и не заменяют отраслевую юридическую проверку. Нет полезного asset → `seo-content-operations`, не более агрессивный pitch.

## 2. Asset gates

1. Зафиксируй вопрос, novel contribution, целевую читательскую задачу и отличие от существующих материалов.
2. Для original research: sampling frame, inclusion/exclusion, период/география, sample size, missingness, metric definitions, bias, consent/анонимизация. Удобная выборка не становится representative.
3. Сохрани допустимые исходники и calculation artifact; все цифры пересчитай инструментом.
4. Для tools: inputs/outputs, documented errors, тестовые случаи, privacy/accessibility. Не собирать private visitor data без отдельного scope/consent.
5. Для experts: настоящий автор/reviewer, подтверждённая квалификация, первичные ссылки, дата; не выдумывать цитаты/должности.
6. Для media: лицензия/атрибуция, alt/captions, provenance/раскрытие synthetic при необходимости. Доступный логотип не означает право его использовать.
7. Выход: asset draft + methodology + редакционное резюме + разрешённые цитаты + limitations. CMS publish — отдельное подтверждение/read-back; unpublished не называть опубликованным.

## 3. Персонализированный DRAFT

Прочитай конкретный материал адресата и существующий тред. Запиши URL и факт для персонализации. Один ясный angle: что нового, кому полезно, почему сейчас, primary source и честное ограничение.
Простой вопрос о fit/предложение данных; без давления, выдуманной срочности и неутверждённой эксклюзивности.
Не требуй dofollow, exact-match anchor или обмен. Не маскируй заинтересованную сторону под независимого пользователя.
Wikipedia не канал self-promotion: не создавать/редактировать страницы о себе в этом workflow. В сообществах — помощь, disclosure связи, правила и отдельное approval.
Контакты минимизировать; публичный email не согласие на массовую рассылку. При сомнении по privacy/маркетинговому праву — hold.

## 4. Approval → send → read-back

Заполни [campaign.md](../templates/campaign.md): sender alias, exact recipients/thread, subject/full text, attachment/link/version, disclosure, CC/BCC (none), расходы/cap, approval evidence.
Используй только одобренные в среде каналы отправки. Для CRM действует политика preview→explicit confirmation→execute→read-back; устаревшие endpoints не копировать. Другие постоянные согласования сохраняются.
Однозначное «да» на показанный обычный email-пакет не требовать подтвердить снова. Но новая аудитория/текст/бюджет, follow-up, CRM write и закупка не разрешены старым approval.
Перед send: сверить sender, suppression/отказ, recent sent/дубли, версию. По одному получателю без CC/BCC, если не утверждено иначе.
После send: точный Sent/thread, from/to/text/time/message ID. При timeout сначала искать результат, не повторять вслепую. Нет read-back → `send unverified`, сообщить, не заявлять успех.
Follow-up только в утверждённом scope/cadence; иначе DRAFT. Opt-out/жалоба/отказ → stop, не новый sender. Ответ адресата не разрешает обещать деньги/встречи/эксклюзивность.

## 5. Earned / paid / verification

Google запрещает links primarily for ranking manipulation. Реклама/спонсорство требуют квалификации `sponsored` или `nofollow`; это отдельный канал, не earned endorsement.[5]
Любую оплату/подарок/договор показать заранее; не покупать ranking credit и удаление rel. Gift в обмен на ссылку не earned.

Для live placement:
1. Перечитать точный URL, timestamp и короткий excerpt.
2. Проверить entity/claim, editorial context, disclosure, paid/earned, href/final target, rel, HTTP/robots. Скрытая реклама/ложный claim = blocker.
3. `live verified` ≠ `indexed` ≠ `SEO effect`; unlinked mention — отдельный результат.
4. Сопоставить referral landing page и разрешённую analytics. Publisher audience/DA не delivered traffic. UTM только уместно/согласованно; не менять canonical SEO URL.
5. Запланировать проверку доступности и исправлений, не обещать вечность ссылки.

## 6. Measurement & stop/go

Определи знаменатели: sent verified/approved recipients, responses/verified sends, qualified placements/contacted prospects, referral leads/attributed sessions. Уточни delivery limitations; bounce, повторные домены, syndicated, sponsored отдельно. Counts/ratios считать кодом.
Сравни periods с seasonality, advertising, releases, migrations и algorithm changes. Малый sample = descriptive, не causal lift. Один publisher не предсказывает весь SEO.
Media mention не AI citation: отдельно engine/locale/date/prompt/URL и повторы в `aieo-visibility`.
**Stop:** права/политики, невалидный asset, неверный адресат, жалобы, cap, нет read-back. **Revise:** нет fit — материал/аудитория, не увеличение спама. **Continue:** подтверждённая ценность; масштаб снова согласовать.

## Evidence basis

Spam policy [5], осторожный disavow [16]; donor [1] — checklist, не proof of ranking lift. См. [sources.md](sources.md).
