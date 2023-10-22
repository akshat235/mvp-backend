from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from auth import auth_bp
from flask_cors import CORS, cross_origin
from models import db


app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc:///?odbc_connect=DRIVER={ODBC Driver 17 for SQL Server};SERVER=092Latitude3410;DATABASE=Sequio_user_1;trusted_connection=yes'

db.init_app(app)

app.register_blueprint(auth_bp, url_prefix='/auth')

with app.app_context():
    db.create_all()


if __name__ == '__main__':
    app.run(debug=True)
