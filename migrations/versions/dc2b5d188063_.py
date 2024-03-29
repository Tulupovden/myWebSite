"""empty message

Revision ID: dc2b5d188063
Revises: 3d7526c4d50d
Create Date: 2021-06-05 05:27:46.245841

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dc2b5d188063'
down_revision = '3d7526c4d50d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('body_html', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('posts', 'body_html')
    # ### end Alembic commands ###
