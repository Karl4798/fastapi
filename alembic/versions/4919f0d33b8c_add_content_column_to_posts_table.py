"""add content column to posts table

Revision ID: 4919f0d33b8c
Revises: 4a9071e3c0ea
Create Date: 2022-07-22 14:28:21.728344

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4919f0d33b8c'
down_revision = '4a9071e3c0ea'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass