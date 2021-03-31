import sys
import os
curr_dir = os.getcwd()
sys.path.append(curr_dir)
from utilities import config_file_functions
from database.Database import Database
from database.accessors.UserConnector import UserConnector
from database.accessors import CreateTags

def main():
  print("Creating database connection...")
  database = Database('database/userLoginInfo.yaml')
  print("Connected to database")
  print("Creating User connection...")
  user_connector = UserConnector(database)
  CreateTags.createTag(database, "test", "this is a test tag")
  CreateTags.findTag(database, "test")
  print("Exiting...")

  database.close_connection
  return database

if __name__ == '__main__':
  main()