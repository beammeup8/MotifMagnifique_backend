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
      host=login_info['host']
    )
    self.cur = self.conn.cursor()

  def callStoredProcedure(procedureName, argsArray):
    self.cur.callproc(procedureName, argsArray.append(0))

  def close_connection(self):
    self.conn.close()