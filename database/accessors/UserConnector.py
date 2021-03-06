import bcrypt
from database.Database import Database
from datetime import timedelta
from base64 import b64encode
from os import urandom

class UserConnector:
  def __init__(self, databaseConnection):
    self.databaseConnection = databaseConnection

  def createUser(self, username, email, fName, lName, password, front_salt):
    back_salt, hashed_password = hashPassword(password = password)
    statement = f"INSERT INTO user (username, email, fName, lName, password, front_salt, back_salt) VALUES (?,?,?,?,?,?,?)"
    args = (username, email, fName, lName, hashed_password, front_salt, back_salt)
    self.databaseConnection.runSQLNoReturn(statement, args)
    
    userId, = self.databaseConnection.runSQL(f"select id from user where username = '{username}'")[0]
    return self.__addAuthToken(userId)

  def authenticate(self, username, authtoken):
    query = "SELECT userId, last_accessed, timeout_len, Now() FROM user, authtoken WHERE user.username=? and authtoken.token=?"
    result = self.databaseConnection.runSQL(query, (username, authtoken))
    if len(result) == 1:
      userId, last_time, timeout, now = result[0]
      latest_valid = last_time + timedelta(minutes = timeout)
      if latest_valid > now:
        self.databaseConnection.runSQLNoReturn(f"UPDATE authtoken SET last_accessed = NOW() WHERE userId = '{userId}'")
        return True
    return False

  def getUserDetails(self, username, authtoken):
    if self.authenticate(username, authtoken):
      query = "select username, email, fName,lName from user where username=?"
      return self.databaseConnection.runSQL(query, (username,))
    else:
      return "None"

  def getSalt(self, username):
    query = "select front_salt, back_salt from user where username=?"
    result = self.databaseConnection.runSQL(query, (username,))
    if len(result) == 1:
      return result[0]
    return "None"


  def checkPassword(self, username, password, salt):
    salt, hashed = hashPassword(password, salt)
    query = "select id from user where username=? and password=?"
    result = self.databaseConnection.runSQL(query, (username, hashed))
    if len(result) != 1:
      return ""
    id, = result[0]
    return self.__addAuthToken(id)

  def __addAuthToken(self, userId):
    token = generateAuthToken()
    statement = f"REPLACE INTO authtoken(userId, token) VALUES ('{userId}', '{token}')"
    self.databaseConnection.runSQLNoReturn(statement)
    return token
    

def generateAuthToken():
    return b64encode(urandom(50)).decode('utf-8')[0:50]

def hashPassword(password, salt = bcrypt.gensalt()):
  hashed_password = bcrypt.hashpw(password, salt)
  return (salt, hashed_password)