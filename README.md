
# Applied AI / SRE Coding Challenge Reference (Python + Java)

A small, interview-practice project that analyzes application/Jenkins logs, groups errors,
estimates severity, and produces remediation suggestions. It is deliberately self-contained:
the default mode works without API keys or internet access. An optional OpenAI adapter is
included in the Python project as an extension point.

## Project structure

```text
deloitte_applied_ai_sre_reference/
├── README.md
├── sample-data/
│   └── application.log
├── sample-output/
│   ├── incident-report.json
│   └── incident-report.csv
├── python/
│   ├── README.md
│   ├── requirements.txt
│   ├── .env.example
│   ├── src/
│   │   └── log_analyzer/
│   │       ├── __init__.py
│   │       ├── analyzer.py
│   │       ├── models.py
│   │       ├── api.py
│   │       └── llm_adapter.py
│   └── tests/
│       └── test_analyzer.py
└── java/
    ├── README.md
    └── pom.xml
    └── src/main/java/com/example/sre/
        ├── LogAnalyzer.java
        ├── Incident.java
        └── Main.java
```

## What this demonstrates

- Parsing semi-structured application logs
- Identifying ERROR / FATAL / EXCEPTION events
- Grouping repeated errors by normalized message
- Severity classification and practical remediation hints
- JSON output and CSV output (easy to open in Excel)
- A minimal FastAPI endpoint in Python
- Unit testing and clear separation of concerns
- Optional LLM integration boundary with safe fallback

## Run Python

Requires Python 3.10+.

```bash
cd python
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

pip install -r requirements.txt
```

Run against the sample log:

```bash
PYTHONPATH=src python -m log_analyzer.analyzer ../sample-data/application.log --json ../sample-output/incident-report.json --csv ../sample-output/incident-report.csv
```

On Windows PowerShell:

```powershell
$env:PYTHONPATH="src"
python -m log_analyzer.analyzer ../sample-data/application.log --json ../sample-output/incident-report.json --csv ../sample-output/incident-report.csv
```

Run tests:

```bash
PYTHONPATH=src pytest -q
```

Run the REST API:

```bash
PYTHONPATH=src uvicorn log_analyzer.api:app --reload
```

Then open `http://127.0.0.1:8000/docs` and POST to `/analyze` with:

```json
{"text": "2026-11-05 10:15:00 ERROR payment-service Database connection timeout"}
```

## Run Java

Requires Java 17+ and Maven.

```bash
cd java
mvn clean package
mvn exec:java -Dexec.args="../../sample-data/application.log"
```

Alternatively, run the packaged main class from your IDE. The Java implementation prints
a JSON-like summary to standard output and writes `incident-report.csv` in the current
directory.

## Interview discussion points

1. **Accuracy:** Current parsing uses keyword and regular-expression heuristics. A production
   version should use structured JSON logs, service metadata, trace IDs, and tested parsers.
2. **AI usage:** Do not send every log line to an LLM. First filter, deduplicate, redact secrets,
   and retrieve relevant runbooks. Use an LLM for summarization and hypotheses, not as the
   sole source of truth.
3. **Safety:** Recommendations are advisory. Automated remediation should require policy checks,
   least-privilege credentials, approval gates, audit logs, and rollback.
4. **Scale:** Move ingestion to a queue/stream, process asynchronously, persist incidents,
   and use a search index / observability platform.
5. **Reliability:** Add timeouts, retries with backoff, rate limits, metrics, tracing, and tests.

## Important

This is a learning/reference starter project, not a production-ready incident-management system.
Do not upload real credentials, customer logs, secrets, or proprietary code to a public GitHub
repository. Review and sanitize sample data before publishing.
