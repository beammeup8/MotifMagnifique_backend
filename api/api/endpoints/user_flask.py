from flask import Blueprint, render_template, request, Response
from flask_httpauth import HTTPBasicAuth

from ..database.accessors.UserConnector import UserConnector
from .validators import validate_params, validate_param
import json
from .response_codes import *
from .response_gen import lst_tuple_response, dict_response


def construct_blueprint(database, userConn, auth):
    user = Blueprint('user', __name__)

    @auth.verify_token
    def verify_token(token):
        userConn.authenticate(token)


    @user.route('/user-details', methods=['GET'])
    def get_user_details():
        field_names = ['username', 'authtoken']
        is_valid, validated_fields = validate_params(request.args, field_names)
        if not is_valid:
            return lst_tuple_response(validated_fields, BAD_REQUEST)
        else:
            details = userConn.getUserDetails(*validated_fields)
            if details != None:
                return dict_response(details, OK)
            else:
                return Response(status=NOT_FOUND)

    @user.route('/new-user', methods=['PUT'])
    def new_user():
        field_names = ['username', 'email', 'fName',
                       'lName', 'password']
        is_valid, validated_fields = validate_params(request.form, field_names)

        if is_valid:
            result = userConn.createUser(*validated_fields)
            if isinstance(result, list):
                return lst_tuple_response(result, DUPLICATE)
            else:
                return Response(result, CREATED)

        return lst_tuple_response(validated_fields, BAD_REQUEST)

    @user.route('/login', methods=['PUT'])
    def login():
        field_names = ['username', 'password']
        is_valid, validated_fields = validate_params(request.form, field_names)

        if is_valid:
            username = validated_fields[0]
            password = validated_fields[1]
            salts = userConn.getSalt(username)
            if salts == None:
                return Response(status=NOT_FOUND)
            result = userConn.checkPassword(username, password, salts[1])
            if result == None:
                return Response(status=NOT_FOUND)
            return result

        return lst_tuple_response(validated_fields, BAD_REQUEST)

    return user
