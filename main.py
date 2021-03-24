import sys
import os
curr_dir = os.getcwd()
sys.path.append(curr_dir)
from utilities import config_file_functions
from database.Database import Database
from database.accessors.UserConnector import UserConnector
from flask import Flask


def main():
  print("Creating database connection...")
  database = Database('database/userLoginInfo.yaml')
  print("Connected to database")
  print("Creating User connection...")
  user_connector = UserConnector(database)
  print("Exiting...")
  database.close_connection
  return 0

if __name__ == '__main__':
  main()