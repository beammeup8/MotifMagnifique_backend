#!/usr/bin/python 
import mariadb 
import yaml

def read_sql_file(filename, cursor):
  sql = ''
  with open(filename) as file:
    sql = file.read()

  commands = sql.split(';')
  for command in commands:
    try:
      if command.strip() != '':
          cursor.execute(command)
    except Exception as msg:
      print("Command skipped: ", msg)


login_info = {}

with open('loginInfo.yaml') as file:
  login_info = yaml.load(file, Loader=yaml.FullLoader)

conn = mariadb.connect(
    user=login_info['username'],
    password=login_info['password'],
    host="localhost")

cur = conn.cursor() 

read_sql_file('setUpScripts/CreateDatabase.sql', cur)
read_sql_file('setUpScripts/CreateTables.sql', cur)
    
conn.close()
