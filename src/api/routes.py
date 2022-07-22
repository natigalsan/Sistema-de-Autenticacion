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

    