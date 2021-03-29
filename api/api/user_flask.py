from flask import Blueprint, render_template, abort
from .database.accessors.UserConnector import UserConnector

def construct_blueprint(database):
    user = Blueprint('user', __name__)

    userConn = UserConnector(database)

    @user.route('/get-salt/<username>', methods=['GET'])
    def get_salt(username):
        salts = userConn.getSalt(username)
        print(salts)
        return ""

    return user