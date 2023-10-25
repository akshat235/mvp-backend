from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask import Blueprint
from models import db, UserAuth, UserData
import hashlib
from argon2 import PasswordHasher


auth_bp = Blueprint("auth", __name__, )

ph = ph = PasswordHasher(time_cost=4, parallelism=8, hash_len=64)

def add_user(username, password, lastName, firstName, dob):
    hashed_password = hash_password(password)
    new_user = UserAuth(username=username, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    temp_user = UserAuth.query.filter_by(username=username).first()
    temp_id = str(temp_user.id)
    hashed_id = hash_password(temp_id)
    new_userData = UserData(username=username, password=hashed_password, userId = hashed_id, dob=dob, firstName = firstName, lastName=lastName )
    db.session.add(new_userData)
    db.session.commit()

def hash_password(password):
    return ph.hash(password)

def check_password(password, hashed_password):
    try:
        ph.verify(hashed_password, password)
        return True
    except:
        return False

@auth_bp.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        try:
            data = request.get_json()
            username = data.get('username')
            password = data.get('password')
            firstName = data.get('firstName')
            lastName = data.get('lastName')
            dob = data.get('dob')

            if not username or not password:
                return jsonify({"error": "Both username and password are required"}), 400

            existing_userAuth = UserAuth.query.filter_by(username=username).first()
            existing_userData = UserData.query.filter_by(username=username).first()

            if existing_userData or existing_userAuth:
                return jsonify({"error": "Username is already taken"}), 400

            add_user(username, password, firstName, lastName, dob)
            return jsonify({"message": "User registered successfully"}), 201

        except Exception as e:
            # Handle and log the error
            print(f"Error during user registration: {str(e)}")
            return jsonify({"error": "An error occurred during registration"}), 500

    


@auth_bp.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')


        if not username or not password:
            return jsonify({"message": "Both username and password are required"}), 400

        user = UserData.query.filter_by(username=username).first()
        if user and check_password(password, user.password):
            user_data = {
                "userId":user.userId,
                "firstname": user.firstName,
                "lastname": user.lastName,
                "username": user.username,
                "dob": user.dob
            }

            return jsonify({"user_data": user_data}), 200
        else:
            return jsonify({"message": "Login failed. Check your credentials"}), 401