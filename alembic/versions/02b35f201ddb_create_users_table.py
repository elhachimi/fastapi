"""create users table

Revision ID: 02b35f201ddb
Revises: aae13ecb6f26
Create Date: 2024-12-15 20:04:12.762230

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "02b35f201ddb"
down_revision: Union[str, None] = "aae13ecb6f26"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("id", sa.Integer, primary_key=True, index=True),
        sa.Column("name", sa.String(50), nullable=False),
    )


def downgrade() -> None:
    op.drop_table("todo")
