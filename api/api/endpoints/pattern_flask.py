from flask import Blueprint, render_template, request, Response
from ..database.accessors.UserConnector import UserConnector
from .validators import validate_params, validate_param
import json
from api.endpoints.response_codes import *
from .response_gen import lst_tuple_response, dict_response


def construct_blueprint(database, userConn):
    pattern = Blueprint('pattern', __name__)
    
    @pattern.route('/details', methods=['GET'])
    def get_user_details():
        return {}

    return pattern
