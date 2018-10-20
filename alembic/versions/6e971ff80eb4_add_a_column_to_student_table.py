"""add a column to student table

Revision ID: 6e971ff80eb4
Revises: 02dbb5f83070
Create Date: 2018-10-20 20:12:07.089477

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6e971ff80eb4'
down_revision = '02dbb5f83070'
branch_labels = None
depends_on = None

def upgrade():
    op.add_column('student_alembic', sa.Column('is_deleted', sa.Integer))


def downgrade():
    op.drop_column('student_alembic', 'is_deleted')

