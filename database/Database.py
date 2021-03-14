import mariadb 
import logging
import yaml
import sys
import os
curr_dir = os.getcwd()
sys.path.append(curr_dir)
from utilities import config_file_functions, data_format_functions

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

  def insertInto(self, table, fields, values):
    fieldsString, valueString = data_format_functions.list_to_sql_fields_and_values(fields)
    queryString = f"INSERT INTO {table} {fieldsString} VALUES {valueString}"
    try:
      self.cur.execute(queryString, values)
      self.conn.commit()
      return True
    except Exception as e:
      print(e)
      return False

  def handleDuplicateKey(self, table, unique_items):
    duplicated = []
    for field, value in unique_items.items():
      queryString = f"SELECT * FROM {table} where {field}=?"
      if len(self.runSQL(queryString, (value,))) != 0:
        duplicated.append((field, value))
    return duplicated

  def runSQL(self, query, parameters = None):
    self.cur.execute(query, parameters)
    return self.cur.fetchall()

  def runSQLNoReturn(self, query, parameters = None):
    self.cur.execute(query, parameters)

  def close_connection(self):
    self.conn.close()