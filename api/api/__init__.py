from flask import Flask
from .endpoints.user_flask import construct_blueprint
from .database.Database import Database

app = Flask(__name__)

database = Database('api/api/database/userLoginInfo.yaml')

user_flask = construct_blueprint(database)
app.register_blueprint(user_flask, url_prefix='/user')