# FastAPI playground

## Installation

### Requirements

- [uv](https://docs.astral.sh/uv/) for Python package and environment management.

On macOS, you can install it with [Homebrew](https://brew.sh/):

```bash
brew install uv
```

For Anass 🍑, you can install it with [Winget](https://winstall.app/apps/astral-sh.uv):

```bash
winget install --id=astral-sh.uv  -e
```

To install dependencies, run:

```bash
uv sync
```

To run database migrations, run:

```bash
uv run alembic upgrade head
```

To start the local server, run:

```bash
uv run fastapi dev src/main.py
```

The server will be running at [http://localhost:8000](http://localhost:8000).
The documentation will be available at [http://localhost:8000/docs](http://localhost:8000/docs).
The redoc will be available at [http://localhost:8000/redoc](http://localhost:8000/redoc).
The openapi.json will be available at [http://localhost:8000/openapi.json](http://localhost:8000/openapi.json).

---

### 🐘 Database migrations

We use [Alembic](https://alembic.sqlalchemy.org/en/latest/) for database migrations.

To create a new migration, run:

```bash
uv run alembic revision -m "Add users table"
```

A new file will be generated: `alembic/versions/<revision_id>_add_users_table.py`.

```python
"""create account table

Revision ID: 1975ea83b712
Revises:
Create Date: 2011-11-08 11:40:27.089406

"""

# revision identifiers, used by Alembic.
revision = '1975ea83b712'
down_revision = None
branch_labels = None

from alembic import op
import sqlalchemy as sa

def upgrade():
    pass

def downgrade():
    pass
```

To run the first migration, run:

```bash
uv run alembic upgrade head
```

### ORM

We use [SQLAlchemy](https://www.sqlalchemy.org/) as the ORM.

### 🚀 FastAPI

We use [FastAPI](https://fastapi.tiangolo.com/) as the web framework.

---

# 📋 TODOs

📝 Tests

- - [ ] Pytest
- - [ ] Coverage

🐳 Docker

- - [ ] Dockerfile
- - [ ] docker-compose

📁 Project structure

- - [ ] 📁 backend
- - [ ] 📁 frontend

🔧 OpenAPI

- - [ ] Code generation
- - [ ] Frontend integration
