#!/usr/bin/python3
"""
API Security and Authentication Techniques using Flask.
"""
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt_identity
)

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'super-secret-key'  # Real işdə bunu gizli saxla
auth = HTTPBasicAuth()
jwt = JWTManager(app)

# İstifadəçilər bazası (Yaddaşda)
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}

# --- Basic Authentication Məntiqi ---
@auth.verify_password
def verify_password(username, password):
    """Basic Auth üçün şifrəni yoxlayır."""
    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        return user
    return None

# --- JWT Xəta İdarəediciləri (Həmişə 401 qaytarmaq üçün) ---
@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401

# --- Endpoints ---

@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    """Basic Auth ilə qorunan marşrut."""
    return "Basic Auth: Access Granted"

@app.route('/login', methods=['POST'])
def login():
    """İstifadəçi girişi və JWT tokenin verilməsi."""
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get('username')
    password = data.get('password')
    user = users.get(username)

    if user and check_password_hash(user['password'], password):
        # Rol məlumatını identity daxilində göndəririk
        access_token = create_access_token(identity=user)
        return jsonify(access_token=access_token)
    
    return jsonify({"error": "Invalid credentials"}), 401

@app.route('/jwt-protected')
@jwt_required()
def jwt_protected():
    """JWT ilə qorunan marşrut."""
    return "JWT Auth: Access Granted"

@app.route('/admin-only')
@jwt_required()
def admin_only():
    """Rol əsaslı giriş (yalnız admin üçün)."""
    current_user = get_jwt_identity()
    if current_user.get('role') != 'admin':
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"

if __name__ == "__main__":
    app.run()
