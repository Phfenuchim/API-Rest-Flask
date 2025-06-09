import uuid
from core.db import db
from modules.access_control.domain.user_role_model import user_roles  # CORRIGIDO

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String(50), unique=True, nullable=False)
    users = db.relationship("modules.users.domain.user_model.User", secondary=user_roles, back_populates="roles")

    