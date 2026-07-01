
from flask import Blueprint, request, jsonify
from models import db, User

user_bp = Blueprint("users", __name__)

# CREATE USER
@user_bp.route("/", methods=["POST"])
def create_user():
    data = request.get_json()

    if not data or not all(k in data for k in ("username", "email", "password")):
        return jsonify({"error": "Dati mancanti"}), 400

    if User.query.filter_by(email=data["email"]).first():
        return jsonify({"error": "Email già registrata"}), 409

    user = User(
        username=data["username"],
        email=data["email"]
    )
    user.set_password(data["password"])

    db.session.add(user)
    db.session.commit()

    return jsonify({
        "message": "Utente creato con successo",
        "user": user.to_dict()
    }), 201

# READ ALL USERS
@user_bp.route("/", methods=["GET"])
def get_users():
    users = User.query.all()
    return jsonify([u.to_dict() for u in users]), 200

# READ SINGLE USER
@user_bp.route("/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = User.query.get_or_404(user_id)
    return jsonify(user.to_dict()), 200

# UPDATE USER
@user_bp.route("/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    user = User.query.get_or_404(user_id)
    data = request.get_json()

    if "username" in data:
        user.username = data["username"]

    if "email" in data:
        user.email = data["email"]

    if "password" in data:
        user.set_password(data["password"])

    db.session.commit()

    return jsonify({
        "message": "Utente aggiornato",
        "user": user.to_dict()
    }), 200

# DELETE USER
@user_bp.route("/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    user = User.query.get_or_404(user_id)

    db.session.delete(user)
    db.session.commit()

    return jsonify({"message": "Utente eliminato"}), 200

# LOGIN
@user_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    user = User.query.filter_by(email=data.get("email")).first()

    if user and user.check_password(data.get("password")):
        return jsonify({
            "message": "Login effettuato con successo",
            "user": user.to_dict()
        }), 200

    return jsonify({"error": "Credenziali non valide"}), 401
