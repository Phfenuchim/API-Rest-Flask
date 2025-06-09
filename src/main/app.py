from flask import Flask
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv
import os

from modules.users.controller.auth_controller import auth_blueprint
from modules.smtp_sendtomail.controller.email_controller import email_blueprint
from modules.users.controller.user_controller import users_blueprint
from modules.access_control.controller.policy_controller import policy_blueprint
from modules.access_control.controller.role_controller import role_blueprint


from core.db import db
from modules.users.domain.user_model import User
from modules.access_control.domain.role_model import Role
from modules.access_control.domain.user_role_model import user_roles

load_dotenv()
def create_app():
    """Factory function to create the Flask app."""
    app = Flask(__name__)
    app.config.from_object("config.Config")
    db.init_app(app)
    JWTManager(app)
    
    # Register Blueprints: padrão de projeto
    app.register_blueprint(users_blueprint)
    app.register_blueprint(auth_blueprint)
    
    app.register_blueprint(policy_blueprint)
    app.register_blueprint(role_blueprint)
    app.register_blueprint(email_blueprint)

    return app

app = create_app()

if __name__ == "__main__":
    
    app.run(debug=True)
