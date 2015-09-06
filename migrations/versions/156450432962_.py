"""empty message

Revision ID: 156450432962
Revises: a950a8d3451
Create Date: 2015-09-05 22:14:36.370955

"""

# revision identifiers, used by Alembic.
revision = '156450432962'
down_revision = 'a950a8d3451'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('thumbnail', sa.String(length=120), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'thumbnail')
    ### end Alembic commands ###
