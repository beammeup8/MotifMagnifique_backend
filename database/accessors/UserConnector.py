
from database.Database import Database

class UserConnector:
  def __init__(self, databaseConnection):
    self.databaseConnection = databaseConnection

  def createUser(self, id, username, email, fName, lName, password, front_salt):
    back_salt, hashed_password = __hashPassword(password)
    pass

  def checkPassword(password, salt):
    hashed = __hashPassword(password, salt)

def __hashPassword(password):
  salt = bcrypt.gensalt()
  return (salt, __hashPassword(password, salt))

def __hashPassword(password, salt):
  hashed_password = bcrypt.hashpw(plain_text_password, salt)
  return hashed_password