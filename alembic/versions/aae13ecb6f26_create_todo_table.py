"""create todo table

Revision ID: aae13ecb6f26
Revises:
Create Date: 2024-12-14 12:40:56.829671

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "aae13ecb6f26"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "todo",
        sa.Column("id", sa.Integer, primary_key=True, index=True),
        sa.Column("title", sa.String(50), nullable=False),
        sa.Column("description", sa.Unicode(200)),
        sa.Column("completed", sa.Boolean),
    )


def downgrade() -> None:
    op.drop_table("todo")
