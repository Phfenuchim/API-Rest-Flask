import uuid
from core.db import db

class Policy(db.Model):
    __tablename__ = 'policies'

    id = db.Column(db.UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    resource = db.Column(db.String(100), nullable=False)
    action = db.Column(db.String(50), nullable=False)
    role_id = db.Column(db.UUID(as_uuid=True), db.ForeignKey('roles.id'), nullable=False)