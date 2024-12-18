"""User forbidden permissions

Revision ID: 23086dc47605
Revises: 3f1664c50dd2
Create Date: 2024-12-15 22:56:23.113286

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '23086dc47605'
down_revision = '3f1664c50dd2'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('service_users', sa.Column('forbidden_actions', postgresql.JSONB(astext_type=sa.Text()), server_default='[]', nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('service_users', 'forbidden_actions')
    # ### end Alembic commands ###