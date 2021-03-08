import mariadb 
import yaml
import sys
import os
curr_dir = os.getcwd()
sys.path.append(curr_dir)
from utilities import config_file_functions

class Database:
  def __init__(self, login_info_file):
    login_info = config_file_functions.getYamlFileContents(login_info_file)
    self.conn = mariadb.connect(
      user=login_info['username'],
      password=login_info['password'],
      host=login_info['host'],
      database=login_info['database']
    )
    self.cur = self.conn.cursor()

  def runSQL(self, query, parameters = None):
    self.cur.execute(query, parameters)
    return self.cur.fetchall()

  def runSQLNoReturn(self, query, parameters = None):
    self.cur.execute(query, parameters)

  def close_connection(self):
    self.conn.close()