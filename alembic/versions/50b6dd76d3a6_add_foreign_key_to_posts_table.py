"""add foreign key to posts table

Revision ID: 50b6dd76d3a6
Revises: 954390015602
Create Date: 2022-07-22 15:29:31.881089

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '50b6dd76d3a6'
down_revision = '954390015602'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id', sa.Integer, nullable=False))
    op.create_foreign_key('posts_user_fk', source_table="posts", referent_table="users",
    local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade() -> None:
    op.drop_constraint('posts_user_fk', table_name="posts")
    op.drop_column('posts', 'owner_id')
    pass