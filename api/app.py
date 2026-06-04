from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)

from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    jwt_required,
    get_jwt_identity
)

app = Flask(__name__)

# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# JWT Secret Key
app.config['JWT_SECRET_KEY'] = 'super-secret-key'

db = SQLAlchemy(app)

jwt = JWTManager(app)


# ==========================
# User Model
# ==========================

class User(db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    username = db.Column(
        db.String(100),
        unique=True,
        nullable=False
    )

    password = db.Column(
        db.String(255),
        nullable=False
    )


# Create tables
with app.app_context():
    db.create_all()


# ==========================
# Register
# ==========================

@app.route('/register', methods=['POST'])
def register():

    data = request.json

    username = data.get('username')
    password = data.get('password')

    existing_user = User.query.filter_by(
        username=username
    ).first()

    if existing_user:

        return jsonify({
            "message": "User already exists"
        }), 400

    hashed_password = generate_password_hash(
        password
    )

    user = User(
        username=username,
        password=hashed_password
    )

    db.session.add(user)
    db.session.commit()

    return jsonify({
        "message": "User registered successfully"
    }), 201


# ==========================
# Login
# ==========================

@app.route('/login', methods=['POST'])
def login():

    data = request.json

    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(
        username=username
    ).first()

    if not user:

        return jsonify({
            "message": "Invalid credentials"
        }), 401

    if not check_password_hash(
        user.password,
        password
    ):

        return jsonify({
            "message": "Invalid credentials"
        }), 401

    access_token = create_access_token(
        identity=str(user.id)
    )

    return jsonify({
        "token": access_token
    })


# ==========================
# Protected Route
# ==========================

@app.route('/profile')
@jwt_required()
def profile():

    current_user_id = get_jwt_identity()

    user = User.query.get(
        int(current_user_id)
    )

    return jsonify({
        "id": user.id,
        "username": user.username
    })


if __name__ == '__main__':
    app.run(debug=True)