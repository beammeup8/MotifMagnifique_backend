from os import urandom
from api.utilities import data_format_functions as dff
import bcrypt
from api.database.Database import Database
from datetime import timedelta
from base64 import b64encode
import sys
import os
curr_dir = os.getcwd()
sys.path.append(curr_dir)


class UserConnector:
    def __init__(self, dbCon):
        self.dbCon = dbCon
        self.table = "user"

    def createUser(self, username, email, fName, lName, password, front_salt=""):
        back_salt, hashed_password = hashPassword(password=password)
        parameter_names = ["username", "email", "fName",
                           "lName", "password", "front_salt", "back_salt"]
        args = (username, email, fName, lName,
                hashed_password, front_salt, back_salt)
        if self.dbCon.insertInto(self.table, parameter_names, args):
            userId, = self.dbCon.runSQL(
                "select id from user where username=?", (username,))[0]
            return self.__addAuthToken(userId)
        else:
            return self.dbCon.handleDuplicateKey(self.table, {"username": username, "email": email})

    def authenticate(self, authtoken):
        query = "SELECT userId, username, last_accessed, timeout_len, Now() FROM authtoken INNER JOIN (user) ON (authtoken.userId = user.id) WHERE authtoken.token=?"
        result = self.dbCon.runSQL(query, (authtoken,))
        if len(result) != 1:
            return None
        userId, username, last_time, timeout, now = result[0]
        latest_valid = last_time + timedelta(minutes=timeout)
        if latest_valid > now:
            self.dbCon.runSQLNoReturn(
                f"UPDATE authtoken SET last_accessed = NOW() WHERE userId = '{userId}'")
            return username
        return None

    def getUserDetails(self, username):
        query = "select username, email, fName,lName from user where username=?"
        details = self.dbCon.runSQL(query, (username,))
        if len(details) == 1:
            return dff.tuples_to_dict(("username", "email", "fName", "lName"), details[0])
        return None

    def getSalt(self, username):
        query = "select front_salt, back_salt from user where username=?"
        result = self.dbCon.runSQL(query, (username,))
        if len(result) == 1:
            return result[0]
        return None

    def getUserId(self, username):
        query = "select id from user where username=?"
        result = self.dbCon.runSQL(query, (username,))
        if len(result) == 1:
            return result[0]
        return None

    def checkPassword(self, username, password, salt):
        salt, hashed = hashPassword(password, salt)
        query = "select id from user where username=? and password=?"
        result = self.dbCon.runSQL(query, (username, hashed))
        if len(result) != 1:
            return None
        id, = result[0]
        return self.__addAuthToken(id)

    def __addAuthToken(self, userId):
        token = generateAuthToken()
        statement = f"REPLACE INTO authtoken(userId, token) VALUES ({userId}, '{token}')"
        self.dbCon.runSQLNoReturn(statement)
        return token


def generateAuthToken():
    return b64encode(urandom(50)).decode('utf-8')[0:50]


def hashPassword(password, salt=bcrypt.gensalt()):
    hashed_password = bcrypt.hashpw(password, salt)
    return (salt, hashed_password)
