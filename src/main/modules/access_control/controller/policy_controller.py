from flask import Blueprint, request, jsonify
from core.db import db
from modules.access_control.domain.policy_model import Policy

policy_blueprint = Blueprint("policies", __name__, url_prefix="/policies")

@policy_blueprint.route("/create", methods=["POST"])
def create_policy():
    data = request.json
    policy = Policy(resource=data["resource"], action=data["action"], role_id=data["role_id"])
    db.session.add(policy)
    db.session.commit()
    return jsonify({"id": str(policy.id), "resource": policy.resource, "action": policy.action}), 201
