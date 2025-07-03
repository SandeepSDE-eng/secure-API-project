 
from flask import Flask
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from routes.auth import auth_bp

app = Flask(__name__)

# Secret Key for JWT (production me env variable me rakhna)
app.config['JWT_SECRET_KEY'] = 'super-secret-key'
jwt = JWTManager(app)

# Enable CORS (for frontend access)
CORS(app)

# Register Auth Routes
app.register_blueprint(auth_bp, url_prefix='/api/auth')

if __name__ == '__main__':
    app.run(debug=True)
