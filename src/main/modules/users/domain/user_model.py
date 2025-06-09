from datetime import datetime
import uuid
from werkzeug.security import generate_password_hash, check_password_hash
from core.db import db
from sqlalchemy.orm import relationship
from modules.access_control.domain.role_model import Role
from modules.access_control.domain.user_role_model import user_roles


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.Text, nullable=False)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    roles = db.relationship("Role", secondary=user_roles, back_populates="users")
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def to_dict(self):
        return {
            "id": str(self.id),
            "username": self.username,
            "email": self.email,
            "is_active": self.is_active,
            "created_at": self.created_at.isoformat()
        }