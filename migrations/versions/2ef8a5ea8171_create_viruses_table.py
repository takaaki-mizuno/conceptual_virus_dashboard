"""create viruses table

Revision ID: 2ef8a5ea8171
Revises: d86568081a85
Create Date: 2021-11-22 21:35:12.010098

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2ef8a5ea8171'
down_revision = 'd86568081a85'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'viruses',
        sa.Column('id', sa.BigInteger, primary_key=True),
        sa.Column('hash', sa.String, nullable=False),
        sa.Column('code', sa.String, nullable=False),
    )
    op.create_index('viruses_hash', 'viruses', ['hash'])


def downgrade():
    op.drop_table('viruses')
