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

def getYamlFileContents(filename):
  with open(filename) as file:
    return yaml.load(file, Loader=yaml.FullLoader)

login_info = getYamlFileContents('loginInfo.yaml')

conn = mariadb.connect(
    user=login_info['username'],
    password=login_info['password'],
    host="localhost")

cur = conn.cursor() 

path = "setUpScripts/"

config = getYamlFileContents(path + "scriptConfig.yaml")

for filename in config['sqlToRun']:
  read_sql_file(path + filename, cur)
  
conn.close()
