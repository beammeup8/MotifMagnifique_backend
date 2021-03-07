import bcrypt
from database.Database import Database
from datetime import timedelta
from base64 import b64encode
import sys
import os
curr_dir = os.getcwd()
sys.path.append(curr_dir)
from utilities import data_format_functions as dff
from os import urandom

class UserConnector:
  def __init__(self, dbCon):
    self.dbCon = dbCon

  def createUser(self, username, email, fName, lName, password, front_salt):
    back_salt, hashed_password = hashPassword(password = password)
    statement = f"INSERT INTO user (username, email, fName, lName, password, front_salt, back_salt) VALUES (?,?,?,?,?,?,?) ON DUPICATE KEY 0+0"
    args = (username, email, fName, lName, hashed_password, front_salt, back_salt)
    self.dbCon.runSQLNoReturn(statement, args)
    
    userId, = self.dbCon.runSQL(f"select id from user where username = '{username}'")[0]
    return self.__addAuthToken(userId)

  def authenticate(self, username, authtoken):
    query = "SELECT userId, last_accessed, timeout_len, Now() FROM user, authtoken WHERE user.username=? and authtoken.token=?"
    result = self.dbCon.runSQL(query, (username, authtoken))
    if len(result) != 1:
      return False
    userId, last_time, timeout, now = result[0]
    latest_valid = last_time + timedelta(minutes = timeout)
    if latest_valid > now:
      self.dbCon.runSQLNoReturn(f"UPDATE authtoken SET last_accessed = NOW() WHERE userId = '{userId}'")
      return True
    return False

  def getUserDetails(self, username, authtoken):
    if self.authenticate(username, authtoken):
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
    statement = f"REPLACE INTO authtoken(userId, token) VALUES ('{userId}', '{token}')"
    self.dbCon.runSQLNoReturn(statement)
    return token
    

def generateAuthToken():
    return b64encode(urandom(50)).decode('utf-8')[0:50]

def hashPassword(password, salt = bcrypt.gensalt()):
  hashed_password = bcrypt.hashpw(password, salt)
  return (salt, hashed_password)