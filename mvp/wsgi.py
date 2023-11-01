from app import app
from flask_cors import CORS, cross_origin 
 
if __name__ == "__main__":
    cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
    app.config['CORS_HEADERS'] = 'Content-Type'
    app.run()
        