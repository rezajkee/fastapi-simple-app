"""Add role to the User model

Revision ID: db6e0ee89ba4
Revises: 88ddd90df649
Create Date: 2023-01-12 15:05:43.848762

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision = 'db6e0ee89ba4'
down_revision = '88ddd90df649'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    user_role = postgresql.ENUM("super_admin", "admin", "user", name="user_role")
    user_role.create(op.get_bind())
    op.add_column('users', sa.Column('role', sa.Enum('super_admin', 'admin', 'user', name='user_role'), server_default='user', nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'role')
    # ### end Alembic commands ###
