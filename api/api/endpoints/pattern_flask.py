from flask import Blueprint, render_template, request, Response
from ..database.accessors.UserConnector import UserConnector
from .validators import validate_params, validate_param
import json
from api.endpoints.response_codes import *
from .response_gen import lst_tuple_response, dict_response


def construct_blueprint(database, userConn):
    pattern = Blueprint('pattern', __name__)

    @pattern.route('/details', methods=['GET'])
    def get_pattern_details():
        field_names = ['username', 'authtoken', 'patternName']
        is_valid, validated_fields = validate_params(request.args, field_names)
        if not is_valid:
            return lst_tuple_response(validated_fields, BAD_REQUEST)
        return {}

    @pattern.route('/new', methods=['PUT'])
    def create_pattern():
        field_names = ['username', 'authtoken', 'patternName']
        is_valid, validated_fields = validate_params(request.args, field_names)
        if not is_valid:
            return lst_tuple_response(validated_fields, BAD_REQUEST)
        return {}

    @pattern.route('/edit', methods=['PUT'])
    def edit_pattern():
        field_names = ['username', 'authtoken', 'patternName']
        is_valid, validated_fields = validate_params(request.args, field_names)
        if not is_valid:
            return lst_tuple_response(validated_fields, BAD_REQUEST)
        return {}

    return pattern
