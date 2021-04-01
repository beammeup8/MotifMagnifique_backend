import sys
import os
curr_dir = os.getcwd()
sys.path.append(curr_dir)
from api.utilities import config_file_functions
from api.database.Database import Database
from api.database.accessors.UserConnector import UserConnector
from flask import Flask


def main():
  print("Creating database connection...")
  database = Database('api/api/database/userLoginInfo.yaml')
  print("Connected to database")
  print("Creating User connection...")
  user_connector = UserConnector(database)
  user_connector.createUser("username", "email@email.com", "user", "name", "something", "front salt")
  print("Exiting...")
  database.close_connection
  return 0

if __name__ == '__main__':
  main()