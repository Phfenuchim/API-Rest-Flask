
from core.db import db

user_roles = db.Table(
    "user_roles",
    db.Column("user_id", db.UUID(as_uuid=True), db.ForeignKey("users.id")),
    db.Column("role_id", db.UUID(as_uuid=True), db.ForeignKey("roles.id"))
)

# NÃO precisa da classe UserRole se for usar só o db.Table!
