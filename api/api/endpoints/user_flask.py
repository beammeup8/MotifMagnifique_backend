from flask import Blueprint, render_template, request, Response
from ..database.accessors.UserConnector import UserConnector
from .validators import validate_params, validate_param
import json
from response_codes import *
from .response_gen import lst_tuple_response


def construct_blueprint(database):
    user = Blueprint('user', __name__)

    userConn = UserConnector(database)

    @user.route('/get-salt', methods=['GET'])
    def get_salt():
        is_valid, username = validate_param(request.args, 'username')
        if not is_valid:
            return lst_tuple_response(username, BAD_REQUEST)
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
                return lst_tuple_response(result, DUPLICATE)
            else:
                return Response(result, CREATED)
        
        return lst_tuple_response(validated_fields, BAD_REQUEST)

    return user