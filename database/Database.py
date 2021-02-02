import mariadb 
import yaml
import sys
import os
curr_dir = os.getcwd()
sys.path.append(curr_dir)
from utilities import *

class Database:
  def __init__(self, login_info_file):
    login_info = configFileFunctions.getYamlFileContents(login_info_file)
    self.conn = mariadb.connect(
      user=login_info['username'],
      password=login_info['password'],
      host="localhost"
    )
    self.cur = self.conn.cursor() 

  def execute_sql_file(self, filename):
    sql = ''
    with open(filename) as file:
      sql = file.read()

    commands = sql.split(';')
    for command in commands:
      try:
        if command.strip() != '':
            self.cur.execute(command)
      except Exception as msg:
        print("Command skipped: ", msg)

  def close_connection(self):
    self.conn.close()