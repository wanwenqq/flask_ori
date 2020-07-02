"""empty message

Revision ID: 57d349141bb9
Revises: 
Create Date: 2020-04-13 10:25:03.352107

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '57d349141bb9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=30), nullable=False),
    sa.Column('_password', sa.String(length=100), nullable=False),
    sa.Column('phone', sa.String(length=50), nullable=False),
    sa.Column('join_time', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('phone')
    )
    op.drop_table('videos')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('videos',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('vid', mysql.VARCHAR(length=50), nullable=True),
    sa.Column('coverUrl', mysql.TEXT(), nullable=True),
    sa.Column('desc', mysql.TEXT(), nullable=True),
    sa.Column('synopsis', mysql.TEXT(), nullable=True),
    sa.Column('title', mysql.VARCHAR(length=100), nullable=True),
    sa.Column('updateTime', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('theme', mysql.VARCHAR(length=10), nullable=True),
    sa.Column('isDelete', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8',
    mysql_engine='MyISAM'
    )
    op.drop_table('user')
    # ### end Alembic commands ###