import unittest
from unittest.mock import *
from database.Database import Database
from database.accessors.UserConnector import UserConnector

class TestGetSalt(unittest.TestCase):

  def setUp(self):
    self.successfulResult = ('frontSalt', 'backSalt')
    self.database = Mock()
    self.database.runSQL.return_value = [self.successfulResult]
    self.user_conn = UserConnector(self.database)

  def test_happy_path(self):
    result = self.user_conn.getSalt('validUserName')
    self.assertEqual(result, self.successfulResult)

  def test_no_results(self):
    self.database.runSQL.return_value = []
    result = self.user_conn.getSalt('badUsername')
    self.assertIsNone(result)

  def test_multiple_results(self):
    self.database.runSQL.return_value = [self.successfulResult, self.successfulResult]
    result = self.user_conn.getSalt('badUsername')
    self.assertIsNone(result)
