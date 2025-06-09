from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from modules.users.service.user_service import UserService
from modules.access_control.service.policy_guard import PolicyGuard
from core.db import db

users_blueprint = Blueprint("users", __name__, url_prefix="/users")

@users_blueprint.route("/", methods=["GET"])
@jwt_required()
def list_users():
    guard = PolicyGuard(db)
    if not guard.has_permission("/users", "read"):
        return jsonify({"msg": "Access Denied"}), 403

    service = UserService(db)
    users = service.list()
    return jsonify([u.to_dict() for u in users])

@users_blueprint.route("/", methods=["POST"])
@jwt_required()
def create_user():
    guard = PolicyGuard(db)
    if not guard.has_permission("/users", "write"):
        return jsonify({"msg": "Access Denied"}), 403

    data = request.json
    service = UserService(db)
    user = service.create(data)
    return jsonify(user.to_dict()), 201

@users_blueprint.route("/<uuid:user_id>", methods=["PUT"])
@jwt_required()
def update_user(user_id):
    guard = PolicyGuard(db)
    if not guard.has_permission("/users", "write"):
        return jsonify({"msg": "Access Denied"}), 403

    data = request.json
    service = UserService(db)
    user = service.update(user_id, data)
    return jsonify(user.to_dict())

@users_blueprint.route("/<uuid:user_id>", methods=["DELETE"])
@jwt_required()
def delete_user(user_id):
    guard = PolicyGuard(db)
    if not guard.has_permission("/users", "delete"):
        return jsonify({"msg": "Access Denied"}), 403

    service = UserService(db)
    service.delete(user_id)
    return jsonify({"msg": "User deleted"})
