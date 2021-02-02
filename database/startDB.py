#!/usr/bin/python 
import mariadb 
import sys
import os
curr_dir = os.getcwd()
sys.path.append(curr_dir)
from utilities import configFileFunctions
from database.Database import Database

print("Starting Database creation...")
db = Database(curr_dir + '/database/loginInfo.yaml')

print("Connecting to database...")
cur = db.cur 

print("Successfully connected...")

path = curr_dir + "/database/setUpScripts/"

config = configFileFunctions.getYamlFileContents(path + "scriptConfig.yaml")

for filename in config['sqlToRun']:
  print("    Running SQL scripts from " + filename + "...")
  db.execute_sql_file(path + filename)
  
print("All SQL scripts run, Closing connection...")
db.close_connection()

print("Connection closed")
