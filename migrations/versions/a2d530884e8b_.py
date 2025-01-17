"""empty message

Revision ID: a2d530884e8b
Revises: 
Create Date: 2022-03-17 20:35:55.486027

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a2d530884e8b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('property_info',
    sa.Column('propertyID', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('propertyTitle', sa.String(length=50), nullable=False),
    sa.Column('no_rooms', sa.Integer(), nullable=False),
    sa.Column('no_bathrooms', sa.Integer(), nullable=False),
    sa.Column('location', sa.String(length=255), nullable=False),
    sa.Column('price', sa.String(length=50), nullable=False),
    sa.Column('propertyType', sa.String(length=50), nullable=False),
    sa.Column('description', sa.String(length=250), nullable=False),
    sa.Column('upload', sa.String(length=50), nullable=False),
    sa.Column('date_created', sa.Date(), nullable=False),
    sa.PrimaryKeyConstraint('propertyID')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('property_info')
    # ### end Alembic commands ###
