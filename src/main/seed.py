import uuid
from flask import Flask
from sqlalchemy import text
from core.db import db
from config import Config
from modules.users.domain.user_model import User
from modules.access_control.domain.role_model import Role
from modules.access_control.domain.policy_model import Policy

app = Flask(__name__)
app.config.from_object('config.Config')
db.init_app(app)

with app.app_context():
    print("⚡ Forçando drop de todas as tabelas com CASCADE...")
    db.session.execute(text("DROP SCHEMA public CASCADE; CREATE SCHEMA public;"))
    db.session.commit()

    print("🧹 Limpando banco...")
    db.create_all()

    # 1. Cria e salva a role
    admin_role = Role(id=uuid.uuid4(), name="admin")
    db.session.add(admin_role)
    db.session.commit()  # Garante que admin_role existe e tem ID persistido

    # 2. Cria user e associa role
    admin_user = User(
        id=uuid.uuid4(),
        username="paulo_admin",
        email="dados@deltaglobalbank.com",
        is_active=True
    )
    admin_user.set_password("QUA!@#$2025")
    admin_user.roles.append(admin_role)
    db.session.add(admin_user)
    db.session.commit()  # Persiste a associação user-role

    # 3. Cria políticas já usando o role_id agora persistido
    default_actions = ["create", "read", "update", "delete"]
    policies = [
        Policy(id=uuid.uuid4(), role_id=admin_role.id, resource="users", action=action)
        for action in default_actions
    ]
    db.session.add_all(policies)
    db.session.commit()

    print("🌱 Seeder executado com sucesso: admin, role e policies criadas.")
