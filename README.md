# FastAPI playground

## Installation

### Requirements

- [uv](https://docs.astral.sh/uv/) for Python package and environment management.

```bash
$ brew install uv
```

To install dependencies, run:

```bash
$ uv sync
```

To run database migrations, run:

```bash
$ uv run alembic upgrade head
```

To start the local server, run:

```bash
$ uv run fastapi dev main.py
```

The server will be running at [http://localhost:8000](http://localhost:8000).
