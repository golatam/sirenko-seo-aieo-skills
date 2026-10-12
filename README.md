# Sirenko SEO/AIEO Skills

Переносимый набор **13 навыков** (12 основных и 1 вспомогательный) для полного SEO/AIEO-цикла: исследование → архитектура → техническая проверка → контент → внедрение по разрешению → продвижение → измерение → следующий цикл. AIEO/AEO/GEO здесь — работа с видимостью в ответах ИИ, не обещание ранжирования или продаж.

Это методики, шаблоны и три локальные утилиты, **не автономная SEO-платформа**. API, аккаунты, внешний rank tracker, crawler, AI-коллектор и смежные host skills не поставляются. Данные клиентов, секреты и частные отчёты в пакет не входят.

## Состав и ответственность

| Навык в `skills/` | Ответственность |
|---|---|
| `seo-aieo` | Точка входа, полный цикл, manifest/evidence, приоритеты, разрешения и приёмка |
| `seo-research-strategy` | Спрос, конкуренты, SERP, семантика, интенты, стратегия |
| `technical-seo-audits` | Crawl/index/rendering, HTML evidence, CWV/schema/логи, инциденты |
| `seo-site-architecture` | Query→URL, структура, перелинковка, programmatic, миграционные handoffs |
| `seo-content-operations` | Бриф, факты, редактура, публикационный пакет, refresh/CRO |
| `aieo-visibility` | Реальные ответы, цитаты, fidelity, native reports и строгий JSONL contract v2 |
| `seo-authority-promotion` | Ссылки, упоминания, PR-активы, черновики outreach, проверка размещений |
| `seo-specializations` | Local/GBP, commerce, international, image/video/news, Яндекс/Алиса |
| `seo-reporting-monitoring` | Сопоставимые измерения, отклонения, эксперименты, очередной цикл |
| `google-search-console-operations` | Discovery, безопасный OAuth, точное property, полнота GSC |
| `rank-tracker-operations` | Topvisor: цена, согласованный запуск, статус и полнота матрицы |
| `ga4-project-reporting` | GA4, трафик, конверсии, ограничения атрибуции и владение отчётом |
| `claim-verification` | Вспомогательный: проверка фактов, цифр, цитат и ответов ИИ по первоисточникам |

Полный процесс и владельцы этапов: [lifecycle](skills/seo-aieo/references/lifecycle.md). Устойчивые ID и передача между этапами: [identity handoff](skills/seo-aieo/references/identity-handoff.md). Необязательные внешние навыки (`competitor-analysis`, `humanizer-ru`) перечислены как **внешние зависимости**, а не часть пакета.

## Локальный запуск без установки навыков

Нужны Python 3.13 и PyYAML из [requirements.txt](requirements.txt). Первые две утилиты ниже используют только стандартную библиотеку. Не устанавливайте зависимости в системный Python с PEP 668: выберите существующее подходящее окружение либо, с разрешения оператора, создайте venv:

```bash
python3 -m venv .venv
. .venv/bin/activate
python3 -m pip install --requirement requirements.txt
```

Команды выполняются из корня checkout. Задайте `TMPDIR` существующим разрешённым scratch-каталогом вне репозитория; runner не использует неявный системный temp. Общие пути и переменные: [WORKSPACE](docs/WORKSPACE.md).

```bash
python3 -B scripts/run_tests.py
python3 -B skills/seo-aieo/scripts/validate_pack.py
python3 -B scripts/check_package.py
```

Runner выполняет unit/CLI, проверку переноса в другой каталог, структуру 13 навыков и ограниченный static/privacy scan. Для точных логов: `python3 -B scripts/run_tests.py --report-dir "$SEO_ARTIFACTS_DIR/portable-check-001"` — каталог должен быть новым и вне checkout. [Подробный scope тестов](docs/TESTING.md).

Синтетический пример, **не статистика бренда**:

```bash
python3 -B skills/aieo-visibility/scripts/summarize_observations.py   skills/aieo-visibility/templates/synthetic-observations.jsonl   --domain example.com --alias 'Example Brand' --allow-synthetic
```

Сохранённый, разрешённый HTML; URL используется только для разрешения относительных ссылок, запросов в сеть нет:

```bash
python3 -B skills/technical-seo-audits/scripts/html_evidence.py   --html "$SEO_ARTIFACTS_DIR/page.html" --url 'https://example.com/'   --out "$SEO_ARTIFACTS_DIR/new-html-evidence.json"
```

Выходной HTML-evidence файл не должен существовать. HTML checker не исполняет JS, не проверяет текущую индексацию/позиции/скорость и не является краулером. AI summarizer проверяет schema v2 и арифметику наблюдений, не истинность источников или полноту коллектора.

## Установка в Claude Code

Пакет ставится как плагин Claude Code прямо из репозитория. Установка меняет только настройки плагинов Claude Code и ничего не запускает из пакета.

```text
/plugin marketplace add golatam/sirenko-seo-aieo-skills
/plugin install seo-aieo@sirenko-seo
```

Навыки плагина получают префикс имени плагина, например `/seo-aieo:seo-aieo`. Проверить без установки можно, запустив Claude Code с флагом `--plugin-dir <путь к checkout>`.

1. Перед установкой прочитайте [SECURITY](docs/SECURITY.md), [SOURCES](SOURCES.md) и запустите тесты.
2. Если те же навыки уже лежат в `~/.claude/skills/`, они будут дублироваться. Сделайте резервную копию и уберите старые копии отдельным решением; пакет ничего не удаляет сам.
3. Подключения (GSC, GA4, Topvisor) проверяйте отдельно минимальными read-only запросами. Отсутствие доступа оставляйте блокером или используйте описанный безопасный fallback; ничего не устанавливается автоматически.

Валидатору можно явно передать `--root skills --external-dependencies docs/host-dependencies.json`. Неизвестный `related_skills` остаётся ошибкой; декларация не подтверждает доступность необязательных внешних навыков.

Пример запроса: «Полный SEO/AIEO-цикл для example.com, рынок US, язык en, цель — квалифицированные заявки. Сначала read-only baseline и план, без публикаций и расходов».

Обновление: прочитать diff версии, запустить тесты, обновить плагин через менеджер плагинов Claude Code (`/plugin`), проверить результат. Автообновлений, hooks, cron и установки MCP в репозитории нет.

## Зависимости, безопасность и границы

- [Необязательные внешние навыки, API и внешний tracker](docs/DEPENDENCIES.md); точный whitelist — [host-dependencies.json](docs/host-dependencies.json).
- [Workspace и приватное хранение](docs/WORKSPACE.md): переменные задаются оператором, не ищут локальные проекты и не читают секреты автоматически.
- [Security](docs/SECURITY.md): no secrets in chat/Git, минимальные права, явные расходы/публикации/доставка, exact-target readback.
- `observed / derived / hypothesis / unknown`, synthetic labels, различие error/zero и schema v2 сохраняются. GSC average position не заменяет rank tracker; readiness не заменяет AI-наблюдения; GA4 не финансовый реестр.
- CI описан в [.github/workflows/tests.yml](.github/workflows/tests.yml), токен только `contents: read`, без secrets и live интеграций. Сетевой доступ нужен лишь для CI checkout/setup/dependency install; сами проверки offline.
- Успех тестов не подтверждает реальную авторизацию GSC/GA4/Topvisor, запуск AI-панели, полный crawl, публикацию в CMS, поведение агента во всех сценариях, рост трафика или выручки. Автоматический scan не является исчерпывающим поиском секретов.

## Лицензия и источники

Оригинальные материалы пакета — [MIT](LICENSE). Доноры использованы выборочно для независимого синтеза, не как установленные плагины или скопированные коллекции. Публичные pinned ссылки, границы лицензирования и сохранённый donor notice: [SOURCES](SOURCES.md). Датированные продуктовые утверждения в reference-файлах требуют повторной проверки перед реальным внедрением.
