# FastAPI playground

## Installation

### Requirements

- [uv](https://docs.astral.sh/uv/) for Python package and environment management.

On macOS, you can install it with [Homebrew](https://brew.sh/):

```bash
$ brew install uv
```

For Anass, you can install it with [Winget](https://winstall.app/apps/astral-sh.uv):

```bash
winget install --id=astral-sh.uv  -e
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
