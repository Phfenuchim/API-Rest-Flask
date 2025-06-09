from flask import Blueprint, request, jsonify
from core.db import db
from modules.access_control.domain.role_model import Role

role_blueprint = Blueprint("roles", __name__, url_prefix="/roles")

@role_blueprint.route("/create", methods=["POST"])
def create_role():
    data = request.json
    role = Role(name=data["name"])
    db.session.add(role)
    db.session.commit()
    return jsonify({"id": str(role.id), "name": role.name}), 201