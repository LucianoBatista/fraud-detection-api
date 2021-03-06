"""Initial migration.

Revision ID: a6f5ccf1071a
Revises: 
Create Date: 2022-01-23 00:31:46.451370

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a6f5ccf1071a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('model',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('modelname', sa.String(length=128), nullable=False),
    sa.Column('precision', sa.Float(), nullable=False),
    sa.Column('recall', sa.Float(), nullable=False),
    sa.Column('accuracy', sa.Float(), nullable=False),
    sa.Column('auc', sa.Float(), nullable=False),
    sa.Column('f1', sa.Float(), nullable=False),
    sa.Column('time', sa.Float(), nullable=False),
    sa.Column('enabled', sa.Boolean(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('modelname')
    )
    op.create_index(op.f('ix_model_created_at'), 'model', ['created_at'], unique=False)
    op.create_table('training_queue',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('dataset', sa.Text(), nullable=False),
    sa.Column('status', sa.String(length=128), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_training_queue_created_at'), 'training_queue', ['created_at'], unique=False)
    op.create_index(op.f('ix_training_queue_updated_at'), 'training_queue', ['updated_at'], unique=False)
    op.create_table('predict',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('transaction', sa.JSON(), nullable=False),
    sa.Column('prediction', sa.Boolean(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('model_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['model_id'], ['model.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_predict_created_at'), 'predict', ['created_at'], unique=False)
    op.create_index(op.f('ix_predict_updated_at'), 'predict', ['updated_at'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_predict_updated_at'), table_name='predict')
    op.drop_index(op.f('ix_predict_created_at'), table_name='predict')
    op.drop_table('predict')
    op.drop_index(op.f('ix_training_queue_updated_at'), table_name='training_queue')
    op.drop_index(op.f('ix_training_queue_created_at'), table_name='training_queue')
    op.drop_table('training_queue')
    op.drop_index(op.f('ix_model_created_at'), table_name='model')
    op.drop_table('model')
    # ### end Alembic commands ###
