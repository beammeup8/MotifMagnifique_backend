from flask import Flask
from flask_httpauth import HTTPTokenAuth

from .endpoints.user_flask import construct_blueprint as make_user_blueprint
from .endpoints.pattern_flask import construct_blueprint as make_pattern_blueprint
from .database.Database import Database
from .database.accessors.UserConnector import UserConnector

app = Flask(__name__)
auth = HTTPTokenAuth(scheme='Bearer')

database = Database('api/api/database/userLoginInfo.yaml')

userConn = UserConnector(database)

user_flask = make_user_blueprint(database, userConn, auth)
app.register_blueprint(user_flask, url_prefix='/user')

pattern_flask = make_pattern_blueprint(database, userConn)
app.register_blueprint(pattern_flask, url_prefix='/pattern')
