"""empty message

Revision ID: d185e6c837ff
Revises: 
Create Date: 2021-02-16 10:59:11.689125

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd185e6c837ff'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('table',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('table_no', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('waiter',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('service',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('table_id', sa.Integer(), nullable=True),
    sa.Column('waiter_id', sa.Integer(), nullable=True),
    sa.Column('arrival', sa.DateTime(), nullable=True),
    sa.Column('exit', sa.DateTime(), nullable=True),
    sa.Column('tip', sa.Numeric(precision=10, scale=2), nullable=True),
    sa.ForeignKeyConstraint(['table_id'], ['table.id'], ),
    sa.ForeignKeyConstraint(['waiter_id'], ['waiter.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('service')
    op.drop_table('waiter')
    op.drop_table('table')
    # ### end Alembic commands ###