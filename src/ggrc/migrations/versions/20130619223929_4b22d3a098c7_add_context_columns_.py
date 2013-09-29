# Copyright (C) 2013 Google Inc., authors, and contributors <see AUTHORS file>
# Licensed under http://www.apache.org/licenses/LICENSE-2.0 <see LICENSE file>
# Created By: 
# Maintained By: 

"""Add context columns for RBAC

Revision ID: 4b22d3a098c7
Revises: 52a791eb9a71
Create Date: 2013-06-19 22:39:29.563353

"""

# revision identifiers, used by Alembic.
revision = '4b22d3a098c7'
down_revision = '52a791eb9a71'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('categories', sa.Column('context_id', sa.Integer(), nullable=True))
    op.add_column('categorizations', sa.Column('context_id', sa.Integer(), nullable=True))
    op.add_column('control_assessments', sa.Column('context_id', sa.Integer(), nullable=True))
    op.add_column('control_controls', sa.Column('context_id', sa.Integer(), nullable=True))
    op.add_column('control_risks', sa.Column('context_id', sa.Integer(), nullable=True))
    op.add_column('control_sections', sa.Column('context_id', sa.Integer(), nullable=True))
    op.add_column('controls', sa.Column('context_id', sa.Integer(), nullable=True))
    op.add_column('cycles', sa.Column('context_id', sa.Integer(), nullable=True))
    op.add_column('data_assets', sa.Column('context_id', sa.Integer(), nullable=True))
    op.add_column('directives', sa.Column('context_id', sa.Integer(), nullable=True))
    op.add_column('documents', sa.Column('context_id', sa.Integer(), nullable=True))
    op.add_column('facilities', sa.Column('context_id', sa.Integer(), nullable=True))
    op.add_column('helps', sa.Column('context_id', sa.Integer(), nullable=True))
    op.add_column('markets', sa.Column('context_id', sa.Integer(), nullable=True))
    op.add_column('meetings', sa.Column('context_id', sa.Integer(), nullable=True))
    op.add_column('object_documents', sa.Column('context_id', sa.Integer(), nullable=True))
    op.add_column('object_people', sa.Column('context_id', sa.Integer(), nullable=True))
    op.add_column('options', sa.Column('context_id', sa.Integer(), nullable=True))
    op.add_column('org_groups', sa.Column('context_id', sa.Integer(), nullable=True))
    op.add_column('pbc_lists', sa.Column('context_id', sa.Integer(), nullable=True))
    op.add_column('people', sa.Column('context_id', sa.Integer(), nullable=True))
    op.add_column('population_samples', sa.Column('context_id', sa.Integer(), nullable=True))
    op.add_column('products', sa.Column('context_id', sa.Integer(), nullable=True))
    op.add_column('program_directives', sa.Column('context_id', sa.Integer(), nullable=True))
    op.add_column('programs', sa.Column('context_id', sa.Integer(), nullable=True))
    op.add_column('projects', sa.Column('context_id', sa.Integer(), nullable=True))
    op.add_column('relationship_types', sa.Column('context_id', sa.Integer(), nullable=True))
    op.add_column('relationships', sa.Column('context_id', sa.Integer(), nullable=True))
    op.add_column('requests', sa.Column('context_id', sa.Integer(), nullable=True))
    op.add_column('responses', sa.Column('context_id', sa.Integer(), nullable=True))
    op.add_column('risk_risky_attributes', sa.Column('context_id', sa.Integer(), nullable=True))
    op.add_column('risks', sa.Column('context_id', sa.Integer(), nullable=True))
    op.add_column('risky_attributes', sa.Column('context_id', sa.Integer(), nullable=True))
    op.add_column('sections', sa.Column('context_id', sa.Integer(), nullable=True))
    op.add_column('system_controls', sa.Column('context_id', sa.Integer(), nullable=True))
    op.add_column('system_systems', sa.Column('context_id', sa.Integer(), nullable=True))
    op.add_column('systems', sa.Column('context_id', sa.Integer(), nullable=True))
    op.add_column('transactions', sa.Column('context_id', sa.Integer(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('transactions', 'context_id')
    op.drop_column('systems', 'context_id')
    op.drop_column('system_systems', 'context_id')
    op.drop_column('system_controls', 'context_id')
    op.drop_column('sections', 'context_id')
    op.drop_column('risky_attributes', 'context_id')
    op.drop_column('risks', 'context_id')
    op.drop_column('risk_risky_attributes', 'context_id')
    op.drop_column('responses', 'context_id')
    op.drop_column('requests', 'context_id')
    op.drop_column('relationships', 'context_id')
    op.drop_column('relationship_types', 'context_id')
    op.drop_column('projects', 'context_id')
    op.drop_column('programs', 'context_id')
    op.drop_column('program_directives', 'context_id')
    op.drop_column('products', 'context_id')
    op.drop_column('population_samples', 'context_id')
    op.drop_column('people', 'context_id')
    op.drop_column('pbc_lists', 'context_id')
    op.drop_column('org_groups', 'context_id')
    op.drop_column('options', 'context_id')
    op.drop_column('object_people', 'context_id')
    op.drop_column('object_documents', 'context_id')
    op.drop_column('meetings', 'context_id')
    op.drop_column('markets', 'context_id')
    op.drop_column('helps', 'context_id')
    op.drop_column('facilities', 'context_id')
    op.drop_column('documents', 'context_id')
    op.drop_column('directives', 'context_id')
    op.drop_column('data_assets', 'context_id')
    op.drop_column('cycles', 'context_id')
    op.drop_column('controls', 'context_id')
    op.drop_column('control_sections', 'context_id')
    op.drop_column('control_risks', 'context_id')
    op.drop_column('control_controls', 'context_id')
    op.drop_column('control_assessments', 'context_id')
    op.drop_column('categorizations', 'context_id')
    op.drop_column('categories', 'context_id')
    ### end Alembic commands ###
