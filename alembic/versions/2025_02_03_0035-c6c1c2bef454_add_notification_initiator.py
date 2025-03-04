"""Add notification initiator

Revision ID: c6c1c2bef454
Revises: d1aa42757f69
Create Date: 2025-02-03 00:35:39.330850

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c6c1c2bef454'
down_revision = 'd1aa42757f69'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('service_notifications', sa.Column('initiator_user_id', sa.Uuid(), nullable=True))
    op.create_foreign_key(None, 'service_notifications', 'service_users', ['initiator_user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'service_notifications', type_='foreignkey')
    op.drop_column('service_notifications', 'initiator_user_id')
    # ### end Alembic commands ###
