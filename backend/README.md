# Weather service API

Starter process for the weather service test. Only `GET /api/health` is implemented. It does not connect to the database yet.

## Setup

From this directory. You need Python 3.14. `uv sync` creates `.venv` and installs the dependencies.

```bash
uv sync
uv run python app.py
```

The process listens on `http://127.0.0.1:5000`.

The database, the measurements file, and what to build are in the parent [README](../README.md).
