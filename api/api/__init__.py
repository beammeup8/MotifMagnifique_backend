from flask import Flask
from flask_httpauth import HTTPTokenAuth

from .endpoints.user_flask import construct_blueprint
from .database.Database import Database
from .database.accessors.UserConnector import UserConnector

app = Flask(__name__)
auth = HTTPTokenAuth(scheme='Bearer')

database = Database('api/api/database/userLoginInfo.yaml')

userConn = UserConnector(database)

user_flask = construct_blueprint(database, userConn, auth)
app.register_blueprint(user_flask, url_prefix='/user')