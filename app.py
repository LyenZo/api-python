from flask import Flask
from config import db, migrate
from dotenv import load_dotenv
import os
from flask_cors import CORS  # Asegúrate de haber instalado flask-cors
from flask_jwt_extended import JWTManager

load_dotenv()

app = Flask(__name__)

# Habilitar CORS globalmente y permitir solicitudes de todo tipo, incluyendo OPTIONS
CORS(app, resources={r"/users/*": {"origins": "*"}}, supports_credentials=True)  # Permite todos los orígenes y credenciales

# Configuración de JWT
app.config['JWT_SECRET_KEY'] = 'qwertyuiop'
jwt = JWTManager(app)

# Configuración de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicialización de la base de datos y migraciones
db.init_app(app)
migrate.init_app(app, db)

# Registro del blueprint de usuario
from routes.user import user_bp
app.register_blueprint(user_bp, url_prefix='/users')

if __name__ == '__main__':
    app.run(debug=True)
