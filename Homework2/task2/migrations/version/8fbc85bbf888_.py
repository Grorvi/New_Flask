"""empty message

Revision ID: 8fbc85bbf888
Revises: 0fde6ee8d405
Create Date: 2024-01-12 16:32:16.967570

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8fbc85bbf888'
down_revision = '0fde6ee8d405'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('mark',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('student_id', sa.Integer(), nullable=True),
    sa.Column('subject_name', sa.String(length=100), nullable=True),
    sa.Column('mark', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['student_id'], ['student.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('mark')
    # ### end Alembic commands ###