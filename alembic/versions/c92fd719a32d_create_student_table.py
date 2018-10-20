"""create student table

Revision ID: c92fd719a32d
Revises: 
Create Date: 2018-10-20 20:10:22.689459

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c92fd719a32d'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.create_table(
        'student_alembic',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50)),
        sa.Column('class_name', sa.String(50)),
        sa.Column('createdOn', sa.DateTime),
        sa.Column('modifiedOn', sa.DateTime)
    )



def downgrade():
    op.drop_table('student_alembic')

