# Проверки и честные границы

## Команды

Из корня checkout, с Python/PyYAML и существующим разрешённым `TMPDIR`:

```bash
python3 -B scripts/run_tests.py
python3 -B scripts/run_tests.py --report-dir "$SEO_ARTIFACTS_DIR/check-001"
```

Второй вариант требует нового каталога **вне** checkout: stdout/stderr каждой стадии и итоговый `summary.json`. Не запускайте оба примера с одним уже существующим output path. Результат — настоящий exit code: 0 только когда все стадии успешны. Скрипт не устанавливает зависимости, не делает git/network/provider calls и не трогает live skills.

## Что проверяется

- Unit tests `validate_pack`: YAML/name/description, ссылки, CSV/JSON, Python compile **без исполнения skill scripts**, unknown related names, archives, duplicates. Дополнительно whitelist host dependencies, typo rejection и запрет объявлять core внешним.
- Unit/CLI tests AI summarizer: strict JSONL schema **v2**, error/unknown/synthetic gates, aliases/domains, identity/dedup, citation/fidelity accounting, locale separation, malformed input. Эти проверки не подтверждают факты источников.
- Unit/CLI tests HTML checker: source tags/duplicates, base/link/robots semantics, JSON-LD syntax, malformed input/limits, offline observation, refusal to overwrite. Не полноценная HTML/schema/index проверка.
- Portable CLI suite: default root вне cwd, explicit root/manifest, empty/invalid declarations, полноценная копия в новый scratch path без live skills, отдельная installation-shaped копия только 13 каталогов в scratch (не live install), synthetic opt-in/label и локальный HTML smoke. Проверены также отказы runner при отсутствии TMPDIR/внутренних output paths и negative pattern fixtures для scanner.
- Whole-pack structural validation: **13/13 навыков**, file references/templates/Python, declared external dependencies. `external_availability_verified=false` не ошибка: доступность host проверяется отдельным разрешённым runtime probe.
- Package-static: ограниченный privacy/pattern/path scan, компиляция всех Python, local Markdown links, обязательные файлы и read-only CI permissions. Отдельный regression guard отклоняет `runner` в workflow/job `env`: этот контекст доступен в `steps.env`, но не на этих ранних уровнях. Это не полный валидатор выражений Actions; [официальная таблица доступности](https://docs.github.com/en/actions/reference/workflows-and-actions/contexts#context-availability).

Runner запускает suites в отдельных Python subprocesses, чтобы discovery импортировал соседние модули корректно. `-B`/`PYTHONDONTWRITEBYTECODE` не засоряют копию pycache. Temp fixtures/relocation создаются внутри заданного `TMPDIR` и удаляются после теста.

## Чего PASS не означает

Не проверены: внешние skills/API авторизация и refresh, UI/report availability в аккаунтах, Topvisor цена/paid collection, полный crawler, сбор реальных AI-ответов, CMS/GBP write/readback, реальные outreach/cron, поведение агентной модели по всем [приёмочным сценариям](../skills/seo-aieo/references/acceptance-tests.md), SEO-эффект и бизнес-результаты.

Проверка YAML workflow и локальный запуск команд **не доказывают hosted GitHub Actions run**. Hosted CI нужно прочитать отдельно после разрешённой публикации. Не заявляется исчерпывающая secret detection; ограничения [SECURITY](SECURITY.md).

Локальная среда, реально использованная для подготовки portable-пакета: Linux, Python 3.13.5, PyYAML 6.0.2. Windows/macOS и другие Python версии отдельно не тестировались. Независимость от исходного пути подтверждается relocation test, не обещанием любой OS.

Точные логи подготовки/преобразований намеренно хранятся **вне** репозитория: они могут содержать локальные пути. Пакет не включает приватный build report. Для новой ревизии сохраняйте собственный новый внешний report directory и проверяйте фактический `summary.json`, а не прежний текст PASS.
