from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from modules.smtp_sendtomail.domain.email_entity import Email
from modules.smtp_sendtomail.service.email_service import EmailService

email_blueprint = Blueprint("email", __name__, url_prefix="/sendtomail")
email_service = EmailService()

@email_blueprint.route("/send-email", methods=["POST"])
@jwt_required()
def send_email():
    data = request.json
    email = Email(
        to_email=data["to"],
        subject=data["subject"],
        body=data["body"],
        cc=data.get("cc", []),
        bcc=data.get("bcc", [])
    )
    success = email_service.send_email(email)
    return jsonify({"message": "Enviado" if success else "Falha ao enviar"}), 200 if success else 500

@email_blueprint.route("/login-check", methods=["GET"])
@jwt_required()
def login_check():
    success = email_service.check_login()
    return jsonify({"status": "Login bem-sucedido" if success else "Falha no login"}), 200 if success else 401

@email_blueprint.route("/status-mail", methods=["GET"])
def status_check():
    success = email_service.check_status()
    return jsonify({"status": "Servidor acessível" if success else "Servidor inacessível"}), 200 if success else 503
