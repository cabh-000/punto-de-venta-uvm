"""Otra migracion de prueba de reversion

Revision ID: 2aa3b7d42ce2
Revises: aca790af9a4e
Create Date: 2024-04-16 23:07:54.674538

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = '2aa3b7d42ce2'
down_revision: Union[str, None] = 'aca790af9a4e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('units', 'segment')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('units', sa.Column('segment', mysql.VARCHAR(length=30), nullable=False))
    # ### end Alembic commands ###
