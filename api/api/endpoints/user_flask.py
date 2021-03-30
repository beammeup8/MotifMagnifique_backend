from flask import Blueprint, render_template, request, Response
from ..database.accessors.UserConnector import UserConnector
from .validators import validate_params
import json
from response_codes import *


def construct_blueprint(database):
    user = Blueprint('user', __name__)

    userConn = UserConnector(database)

    @user.route('/get-salt', methods=['GET'])
    def get_salt():
        username = request.args.get('username')
        salts = userConn.getSalt(username)
        if salts != None:
            return salts[0]
        return Response(NOT_FOUND)

    @user.route('/new-user', methods=['PUT'])
    def create_user():
        field_names = ['username', 'email', 'fName', 'lName', 'password', 'front_salt']
        is_valid, validated_fields = validate_params(request.form, field_names)
        
        if is_valid:
            result = userConn.createUser(*validated_fields)
            if isinstance(result, list):
                return Response(json.dumps(dict(result)), DUPLICATE)
            else:
                return Response(result, CREATED)
        
        return Response(json.dumps(dict(validated_fields)), BAD_REQUEST)

    return user