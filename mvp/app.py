from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
from auth import auth_bp
from test_handler import test_bp
from dashboard import dashboard_bp
from flask_cors import CORS, cross_origin
from models import db, Question
from mongoengine import connect
import mongoengine


app = Flask(__name__)
CORS(app)
app.secret_key = 'dljsaklqk24e21cjn!Ew@@dsa5'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc:///?odbc_connect=DRIVER={ODBC Driver 17 for SQL Server};SERVER=092Latitude3410;DATABASE=Sequio_user_1;trusted_connection=yes'


# conn_str = (
#     "Driver={ODBC Driver 17 for SQL Server};"
#     "Server=sql305.infinityfree.com;"
#     "Database=if0_35129443_user;"
#     "UID=if0_35129443;"
#     "PWD=BlGZx13uB9;"
# )


app.config['SQLALCHEMY_DATABASE_URI'] = "mssql+pyodbc://if0_35129443:BlGZx13uB9@sql305.infinityfree.com/if0_35129443_user?driver=ODBC+Driver+17+for+SQL+Server"


# app.config['MONGODB_SETTINGS'] = {
#     'db': 'DummyQuestions',
#     'host': 'mongodb://localhost:27017'
# }

app.config['SESSION_TYPE'] = 'filesystem'   
app.config['SESSION_PERMANENT'] = False
# session(app)

mongoengine.register_connection(
    alias='default',
    name='cat_exam',  
    host='mongodb://localhost:27017')
  

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


if __name__ == '__main__':
    app.run(debug=True)
