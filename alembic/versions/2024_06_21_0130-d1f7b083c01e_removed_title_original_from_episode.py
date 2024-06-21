"""Removed title_original from episode

Revision ID: d1f7b083c01e
Revises: 3ef5732b5d63
Create Date: 2024-06-21 01:30:59.939718

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd1f7b083c01e'
down_revision = '3ef5732b5d63'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('service_content_anime_episodes', 'title_original')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('service_content_anime_episodes', sa.Column('title_original', sa.VARCHAR(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###