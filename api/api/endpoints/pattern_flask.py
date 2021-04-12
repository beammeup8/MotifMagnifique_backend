from flask import Blueprint, render_template, request, Response
from flask_httpauth import HTTPBasicAuth

from ..database.accessors.UserConnector import UserConnector
from .validators import validate_params, validate_param
import json
from api.endpoints.response_codes import *
from .response_gen import lst_tuple_response, dict_response


def construct_blueprint(database, patternConn, auth):
    pattern = Blueprint('pattern', __name__)

    @pattern.route('/details', methods=['GET'])
    @auth.login_required
    def get_pattern_details():
        field_names = ['pattern_id']
        is_valid, validated_fields = validate_params(request.args, field_names)
        if not is_valid:
            return lst_tuple_response(validated_fields, BAD_REQUEST)
        return {}

    @pattern.route('/new', methods=['PUT'])
    @auth.login_required
    def create_pattern():
        field_names = ['pattern_name']
        optional_field_names = ['description', 'tags', 'price', 'link', 'images', 'fabricType']
        is_valid, validated_fields = validate_params(request.args, field_names, optional_field_names)
        if not is_valid:
            return lst_tuple_response(validated_fields, BAD_REQUEST)
        return {}

    return pattern
