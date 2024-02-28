"""Removed created field from collection content

Revision ID: 55e4300b8247
Revises: 3da0988d8d0b
Create Date: 2024-02-23 14:30:20.039039

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '55e4300b8247'
down_revision = '3da0988d8d0b'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('service_collection_content', 'created')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('service_collection_content', sa.Column('created', postgresql.TIMESTAMP(), autoincrement=False, nullable=False))
    # ### end Alembic commands ###
