from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from core.db import db
from modules.users.service.user_service import UserService

auth_blueprint = Blueprint("auth_user", __name__)

@auth_blueprint.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    service = UserService(db)
    user = service.authenticate_user(username, password)
    if not user:
        return jsonify({"msg": "Credenciais inválidas"}), 401

    access_token = create_access_token(identity=user.username)
    return jsonify(access_token=access_token), 200
