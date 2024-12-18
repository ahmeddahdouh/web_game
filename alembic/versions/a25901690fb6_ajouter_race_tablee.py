"""ajouter race tablee

Revision ID: a25901690fb6
Revises: ad56fec4a714
Create Date: 2024-12-18 12:56:11.667918

"""
from typing import Sequence, Union
import sqlmodel
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a25901690fb6'
down_revision: Union[str, None] = 'ad56fec4a714'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('equipment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('type', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('weight', sa.Integer(), nullable=False),
    sa.Column('slot', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('allowed_classes', sa.JSON(), nullable=True),
    sa.Column('strength', sa.Integer(), nullable=False),
    sa.Column('agility', sa.Integer(), nullable=False),
    sa.Column('speed', sa.Integer(), nullable=False),
    sa.Column('chance', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('equipment')
    # ### end Alembic commands ###