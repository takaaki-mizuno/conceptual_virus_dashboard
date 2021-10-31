"""create snapshots table

Revision ID: d86568081a85
Revises: 2a3c7799d590
Create Date: 2021-10-31 18:23:32.184926

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd86568081a85'
down_revision = '2a3c7799d590'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'snapshots',
        sa.Column('id', sa.BigInteger, primary_key=True),
        sa.Column('creature_id', sa.BigInteger, nullable=False),
        sa.Column('sent_at', sa.Integer, nullable=False),
        sa.Column('status', sa.JSON, nullable=False)
    )
    op.create_index('snapshots_creature', 'snapshots', ['creature_id', 'sent_at'])


def downgrade():
    pass
