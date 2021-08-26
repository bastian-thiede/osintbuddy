"""Added search and usersearch tables

Revision ID: 731ee07393f7
Revises: 779e95ccddba
Create Date: 2021-08-26 19:01:32.901286

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '731ee07393f7'
down_revision = '779e95ccddba'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('search',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('query', sa.String(), nullable=False),
    sa.Column('created', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_search_id'), 'search', ['id'], unique=False)
    op.create_table('usersearch',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('project_id', sa.Integer(), nullable=True),
    sa.Column('search_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['project_id'], ['project.id'], ),
    sa.ForeignKeyConstraint(['search_id'], ['search.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_usersearch_id'), 'usersearch', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_usersearch_id'), table_name='usersearch')
    op.drop_table('usersearch')
    op.drop_index(op.f('ix_search_id'), table_name='search')
    op.drop_table('search')
    # ### end Alembic commands ###