"""empty message

Revision ID: 2e1228768e0a
Revises: 
Create Date: 2021-03-27 15:58:00.062423

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2e1228768e0a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('theater',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('musical',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('num', sa.String(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('start', sa.DateTime(), nullable=False),
    sa.Column('end', sa.DateTime(), nullable=False),
    sa.Column('runtime', sa.String(), nullable=True),
    sa.Column('showtime', sa.String(), nullable=True),
    sa.Column('rating', sa.String(), nullable=True),
    sa.Column('price', sa.String(), nullable=True),
    sa.Column('casting', sa.String(), nullable=True),
    sa.Column('url', sa.String(), nullable=True),
    sa.Column('theater_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['theater_id'], ['theater.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('musical')
    op.drop_table('theater')
    # ### end Alembic commands ###