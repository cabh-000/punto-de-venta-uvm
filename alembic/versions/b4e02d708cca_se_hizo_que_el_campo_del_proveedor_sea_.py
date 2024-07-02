"""Se hizo que el campo del proveedor sea opcional

Revision ID: b4e02d708cca
Revises: 14f7a031e901
Create Date: 2024-07-02 12:06:51.882765

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = 'b4e02d708cca'
down_revision: Union[str, None] = '14f7a031e901'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('purchases', 'supplier_id',
               existing_type=mysql.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('purchases', 'supplier_id',
               existing_type=mysql.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###
