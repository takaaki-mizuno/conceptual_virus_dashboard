"""create creatures table

Revision ID: 2a3c7799d590
Revises: 
Create Date: 2021-10-31 18:14:47.998110

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '2a3c7799d590'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'creatures',
        sa.Column('id', sa.BigInteger, primary_key=True),
        sa.Column('ip_address', sa.String(32), nullable=False),
        sa.Column('identity_key', sa.String(64), nullable=False),
        sa.Column('is_active', sa.Boolean, nullable=False),
        sa.Column('last_ping_sent_at', sa.Integer, nullable=False),
        sa.Column('first_ping_sent_at', sa.Integer, nullable=False),
    )
    op.create_index('creatures_address', 'creatures', ['ip_address'])
    op.create_index('creatures_identity_key', 'creatures', ['identity_key'])
    op.create_index('creatures_latest_activity', 'creatures', ['last_ping_sent_at'])


def downgrade():
    op.drop_table('creatures')
