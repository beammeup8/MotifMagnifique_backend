from flask import Response
import json


def lst_tuple_response(result, status):
    return Response(json.dumps(dict(result)), status)


def dict_response(result, status):
    return Response(json.dumps(result), status)
