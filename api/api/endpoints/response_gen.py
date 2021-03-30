from flask import Response
import json

def lst_tuple_response(result, status):
  Response(json.dumps(dict(result)), status)