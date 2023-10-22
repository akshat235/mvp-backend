from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class UserAuth(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)


class UserData(db.Model):
    userId = db.Column(db.String(255), primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    firstName = db.Column(db.String(50), nullable=False)
    lastName = db.Column(db.String(50), nullable=False)
    dob = db.Column(db.Date, nullable=False)
    password = db.Column(db.String(255), nullable=False)