# Python implementation

Python 3.10+.

## Run

```bash
pip install -r requirements.txt
PYTHONPATH=src python -m log_analyzer.analyzer ../sample-data/application.log --json ../sample-output/incident-report.json --csv ../sample-output/incident-report.csv
```

## API

```bash
PYTHONPATH=src uvicorn log_analyzer.api:app --reload
```

POST `/analyze` with JSON body `{"text": "ERROR database timeout"}`.

## Tests

```bash
PYTHONPATH=src pytest -q
```

The default analyzer is deterministic and offline. `llm_adapter.py` shows where an LLM
summary could be plugged in; it intentionally does not make network calls or require a key.
