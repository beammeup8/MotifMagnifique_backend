import unittest
from unittest.mock import *
from database.Database import Database
from database.accessors.CreateTags import  CreateTags
import datetime


class TestCreate(unittest.TestCase):

  def setUp(self):
    self.id = 7
    self.authtoken = 'some auth token'
    self.database = Mock()
    self.user_conn = UserConnector(self.database)
    self.database.runSQL.return_value = [(self.id,)]
    self.database.insertInto.return_value = True
    self.database.handleDuplicateKey.return_value = [("username", "invalid")]
 
  def test_happy_path(self):
    result = self.user_conn.createUser("username", "email@email.com", "user", "name", "password", "front_salt")
    self.assertIsInstance(result, str)

  def test_create_fail(self):
    self.database.insertInto.return_value = False
    result = self.user_conn.createUser("username", "email@email.com", "user", "name", "password", "front_salt")
    self.assertIsInstance(result, list)
    