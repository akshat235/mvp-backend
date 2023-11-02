from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
from auth import auth_bp
from test_handler import test_bp
from dashboard import dashboard_bp
from flask_cors import CORS, cross_origin
from models import db, Question
from mongoengine import connect
import mongoengine
import sqlalchemy_cockroachdb


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.secret_key = 'dljsaklqk24e21cjn!Ew@@dsa5'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc:///?odbc_connect=DRIVER={ODBC Driver 17 for SQL Server};SERVER=092Latitude3410;DATABASE=Sequio_user_1;trusted_connection=yes'


# conn_str = (
#     "Driver={ODBC Driver 17 for SQL Server};"
#     "Server=sql305.infinityfree.com;"
#     "Database=if0_35129443_user;"
#     "UID=if0_35129443;"
#     "PWD=BlGZx13uB9;"
# )


# app.config['SQLALCHEMY_DATABASE_URI'] = "cockroachdb://sequio:6TWp3jo7ABWTEZQyzzaW5A@funny-monkey-3740.g95.cockroachlabs.cloud:26257/user?sslmode=verify-full"
app.config['SQLALCHEMY_DATABASE_URI'] = "cockroachdb://sequio:6YOZGm7rmeM-8N4g2v5TOg@elder-thrush-3741.g95.cockroachlabs.cloud:26257/user?sslmode=allow"


# app.config['MONGODB_SETTINGS'] = {
#     'db': 'DummyQuestions',
#     'host': 'mongodb://localhost:27017'
# }

app.config['SESSION_TYPE'] = 'filesystem'   
app.config['SESSION_PERMANENT'] = False
# session(app)

# mongoengine.register_connection(
#     alias='default',
#     name='cat_exam',  
#     host='mongodb://localhost:27017')
  

mongoengine.register_connection(
    alias='default',
    name='response',
    host='mongodb+srv://sequio:nkY9KPEPZmNhBYYx@cluster0.jyovip1.mongodb.net/?retryWrites=true&w=majority/user') 
  

# mongoengine.connect('DummyQuestions', host='mongodb://localhost:27017')

# connect(
#     alias='default',
#     host=app.config['MONGODB_SETTINGS']['host']   
# )

db.init_app(app)

app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(dashboard_bp, url_prefix='/dashboard')
app.register_blueprint(test_bp, url_prefix='/test')

with app.app_context():
    db.create_all()


#if __name__ == '__main__':
   # app.run(debug=True)
