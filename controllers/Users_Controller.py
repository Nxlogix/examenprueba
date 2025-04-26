from models.User import Usuario
from flask import jsonify
from config import db
from flask_jwt_extended import create_access_token

def create_usuario(nombre, email, password):
    try:
        nuevo_usuario = Usuario(nombre, email, password)
        db.session.add(nuevo_usuario)
        db.session.commit()
        return jsonify(nuevo_usuario.to_dict()), 201
    except Exception as e:
        print(f"ERROR {e}")
        return jsonify({'msg': 'Error al crear el nuevo usuario'}), 500

def login_usuario(email, password):
    try:
        usuario = Usuario.query.filter_by(email=email).first()
        
        if usuario and usuario.check_password(password):
            access_token = create_access_token(identity=usuario.id)
            return jsonify({
                'access_token': access_token,
                'usuario': {
                    "id": usuario.id,
                    "nombre": usuario.nombre,
                    "email": usuario.email
                }
            })
        return jsonify({"msg": "Datos incorrectos"}), 401
    except Exception as e:
        print(f"ERROR {e}")
        return jsonify({'msg': 'Error en el inicio de sesion'}), 500

def get_all_usuarios():
    try:
        usuarios = [usuario.to_dict() for usuario in Usuario.query.all()]
        return jsonify(usuarios)
    except Exception as error:
        print(f"ERROR {error}")
        return jsonify({'msg': f'Error al obtener los usuarios: {error}'}), 500