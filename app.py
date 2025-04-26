import os
from flask import Flask
from config import db, migrate
from dotenv import load_dotenv
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flasgger import Swagger

# Cargar variables de entorno
load_dotenv()

# Inicialización de la aplicación Flask
app = Flask(__name__)

# Permitir solo el dominio de tu frontend de Amplify
CORS(app, resources={r"/*": {"origins": "https://main.df4r7dk920gqc.amplifyapp.com"}}) # cambialo por tu link de amplify 

# Configuración de JWT y base de datos
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'Clave secreta para examen')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Configuración de Swagger (Flasgger)
app.config['SWAGGER'] = {
    'title': 'API de Usuarios - Examen',
    'uiversion': 3
}
swagger = Swagger(app)


# Inicialización de las extensiones de la base de datos y JWT
db.init_app(app)
migrate.init_app(app, db)
jwt = JWTManager(app)

# Ruta de prueba
@app.route('/')
def home():
    return 'API prueba'

# Registrar las rutas del blueprint de usuarios
from routes.user import usuario_bp
app.register_blueprint(usuario_bp, url_prefix='/usuarios')

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run(debug=True)

    