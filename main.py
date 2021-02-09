import sys
import os
curr_dir = os.getcwd()
sys.path.append(curr_dir)
from utilities import configFileFunctions
from database.Database import Database
from database.accessors.UserConnector import UserConnector

def main():
  print("Creating database connection...")
  database = Database('database/userLoginInfo.yaml')
  print("Connected to database")
  print("Creating User connection...")
  userConnector = UserConnector(database)
  return 0

if __name__ == '__main__':
  main()