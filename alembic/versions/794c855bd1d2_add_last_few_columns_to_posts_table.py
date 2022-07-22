"""add last few columns to posts table

Revision ID: 794c855bd1d2
Revises: 50b6dd76d3a6
Create Date: 2022-07-22 15:43:59.446624

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '794c855bd1d2'
down_revision = '50b6dd76d3a6'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('published', sa.Boolean(),
                  nullable=False, server_default='TRUE'))
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(
        timezone=True), nullable=False, server_default=sa.text('now()')))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass