"""add role to users table

Revision ID: 256734c5a2f5
Revises: bae9588772b2
Create Date: 2026-07-23 23:36:50.387703

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "256734c5a2f5"
down_revision: Union[str, Sequence[str], None] = "bae9588772b2"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


user_role_enum = sa.Enum(
    "ADMIN",
    "USER",
    name="userrole"
)


def upgrade() -> None:
    """Upgrade schema."""

    # Create PostgreSQL ENUM type
    user_role_enum.create(op.get_bind(), checkfirst=True)

    # Add the column
    op.add_column(
        "users",
        sa.Column(
            "role",
            user_role_enum,
            nullable=False,
            server_default="USER"
        )
    )

    # Remove the default for future inserts.
    # SQLAlchemy's model default will handle new users.
    op.alter_column(
        "users",
        "role",
        server_default=None
    )


def downgrade() -> None:
    """Downgrade schema."""

    op.drop_column(
        "users",
        "role"
    )

    user_role_enum.drop(
        op.get_bind(),
        checkfirst=True
    )