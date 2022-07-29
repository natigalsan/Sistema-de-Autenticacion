"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User
from api.utils import generate_sitemap, APIException
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
import datetime


api = Blueprint('api', __name__)


@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }

    return jsonify(response_body), 200


@api.route('/register', methods=['POST'])
def register():
    # en mi variable body voy a guardar los datos que necesito cuando un user se registra-->
    body = request.get_json() 
    # y voy  a retornar en formato jsonify() la variable donde guardo los datos que he recogido del user
    # cuando alguien se registra debe mi app comprobar si existe ya ese registro-->
    # print(body['email'])
    # mirar SQLAlquemis 
    OnePeople = User.query.filter_by(email=body['email']).first() 
    # body['email']-->es donde se ha recogido la información del usuario que se acaba de registrar y donde debe hacer la búsqueda con OnePeople
    if OnePeople:
        return jsonify({"ERROR": "este usuario ya está registrado"}), 418

    else: 
    # en caso de no estar registrado le vamos a pedir que registre al user: 
    # SQL alquemis--> Insert newUser
        newUser = User(email=body['email'], password=body['password'], is_active = True)
        db.session.add(newUser)
        db.session.commit()
        return jsonify(body), 201
        # podemos comprobarlo con posmant ...y efectivamente funciona :D 
        # a continuación crearé desde el front ('/private') el registro

#---------------------------- RUTA PARA INICIAR SESIÓN------------------------------
@api.route('/login', methods=['POST'])
def login():
    # Para inciar sesión necesito capturar los datos de usuario y contraseña para ello hago lo siguiente: 
    body = request.get_json() 
    # cuando usuario y contraseña sean correctos --> genero un token y luego lo return... en formato jsonify
    # pero debo comprobar si el usuario existe cuando hacen el login: 
    OnePeople = User.query.filter_by(email=body['email'], password = body['password']).first() 
    if OnePeople:
        # si existe en mi base de datos un ususario con estos datos --> le creamos su token
        token = create_access_token(identity = body['email'])
        return jsonify({'access_token': token, "mensaje": "Bienvenido, acaba de iniciar sesión"}), 200
        # en caso contrario de no existir: 

    else: 
        return jsonify({"error": "El usuario no existe"}), 418



#voy a crear una ruta que necesita del token: 
@api.route('/private', methods=['GET'])
@jwt_required()
def private():
    identidad = get_jwt_identity()
    return jsonify({"mensaje": "Tienes permiso para iniciar sesión", "permiso": True, "email": identidad}), 200
    # en Postman mando el token poniendo Autorización con método GET: Type: "Bearer Token"