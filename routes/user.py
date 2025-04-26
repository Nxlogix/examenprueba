from flask import Blueprint, jsonify, request
from controllers.Users_Controller import create_usuario, login_usuario, get_all_usuarios

usuario_bp = Blueprint('usuarios', __name__)

@usuario_bp.route('/', methods=['POST'])
def user_store():
        """
        Crear un nuevo usuario
        ---
        tags:
        - Usuarios
        requestBody:
        required: true
        content:
            application/json:
            schema:
                type: object
                required:
                - email
                - nombre
                - password
                properties:
                email:
                    type: string
                    example: usuario@example.com
                nombre:
                    type: string
                    example: Juan Pérez
                password:
                    type: string
                    example: contrasena123
        responses:
        201:
            description: Usuario creado exitosamente
        400:
            description: Faltan campos requeridos
        """
        data = request.get_json()
        email = data.get('email')
        nombre = data.get('nombre')
        password = data.get('password')

        if not all([email, nombre, password]):
            return jsonify({"error": "Rellena todos los campos por favor"}), 400
        
        return create_usuario(nombre, email, password)


@usuario_bp.route('/login', methods=['POST'])
def login_usuario_route():
        """
        Iniciar sesión con un usuario existente
        ---
        tags:
        - Usuarios
        requestBody:
        required: true
        content:
            application/json:
            schema:
                type: object
                required:
                - email
                - password
                properties:
                email:
                    type: string
                    example: usuario@example.com
                password:
                    type: string
                    example: contrasena123
        responses:
        200:
            description: Inicio de sesión exitoso
        400:
            description: Datos de entrada incompletos
        401:
            description: Credenciales incorrectas
        """
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')

        if not email or not password:
            return jsonify({"error": "El email y la contraseña son requeridos para iniciar sesión"}), 400
        
        return login_usuario(email, password)


@usuario_bp.route('/obtener', methods=['GET'])
def get_usuarios():
        """
        Obtener todos los usuarios
        ---
        tags:
        - Usuarios
        responses:
        200:
            description: Lista de usuarios obtenida exitosamente
            content:
            application/json:
                schema:
                type: array
                items:
                    type: object
                    properties:
                    id:
                        type: integer
                        example: 1
                    nombre:
                        type: string
                        example: Juan Pérez
                    email:
                        type: string
                        example: usuario@example.com
        500:
            description: Error del servidor
        """
        return get_all_usuarios()