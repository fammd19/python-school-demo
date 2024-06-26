"""Create initial models

Revision ID: 74892fd3ce49
Revises: 
Create Date: 2024-06-27 08:17:36.418501

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '74892fd3ce49'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('courses',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('students',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('degree', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('enrolments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('course_id', sa.Integer(), nullable=True),
    sa.Column('student_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['course_id'], ['courses.id'], ),
    sa.ForeignKeyConstraint(['student_id'], ['students.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('enrolments')
    op.drop_table('students')
    op.drop_table('courses')
    # ### end Alembic commands ###
