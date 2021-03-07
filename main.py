import sys
import os
curr_dir = os.getcwd()
sys.path.append(curr_dir)
from utilities import config_file_functions
from database.Database import Database
from database.accessors.UserConnector import UserConnector

def main():
  print("Creating database connection...")
  database = Database('database/userLoginInfo.yaml')
  print("Connected to database")
  print("Creating User connection...")
  user_connector = UserConnector(database)
  # create a dummy user
  authtoken = user_connector.createUser("pythonPerson", "fake@email.com", "python", "person", "password", "yyyyy")
  print(user_connector.getUserDetails('pythonPerson', authtoken))
  front_salt, back_salt = user_connector.getSalt('pythonPerson')
  print(user_connector.checkPassword('pythonPerson', 'password', back_salt))
  print("Exiting...")
  return 0

if __name__ == '__main__':
  main()