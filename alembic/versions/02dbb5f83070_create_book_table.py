"""create book table

Revision ID: 02dbb5f83070
Revises: c92fd719a32d
Create Date: 2018-10-20 20:10:34.460059

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '02dbb5f83070'
down_revision = 'c92fd719a32d'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'book_alembic',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('title', sa.String(50))
    )


def downgrade():
i    op.drop_table('book_alembic')

