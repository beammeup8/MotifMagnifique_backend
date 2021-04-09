import unittest
from unittest.mock import *
from ...database.Database import Database
from ...database.accessors.UserConnector import UserConnector

class TestGetUserDetails(unittest.TestCase):

  def setUp(self):
    self.successfulResult = ('fakeUser', 'fake@email.com', 'Fake', 'User')
    self.database = Mock()
    self.database.runSQL.return_value = [self.successfulResult]
    self.user_conn = UserConnector(self.database)

  def test_happy_path(self):
    username, email, fName, lName = self.successfulResult
    result = self.user_conn.getUserDetails(username)
    self.assertEqual(len(result), len(self.successfulResult))
    self.assertEqual(result['username'], username)
    self.assertEqual(result['email'], email)
    self.assertEqual(result['fName'], fName)
    self.assertEqual(result['lName'], lName)

  def test_no_results(self):
    self.database.runSQL.return_value = []
    result = self.user_conn.getUserDetails('badUsername')
    self.assertIsNone(result)

  def test_multiple_results(self):
    self.database.runSQL.return_value = [self.successfulResult, self.successfulResult]
    result = self.user_conn.getUserDetails('badUsername')
    self.assertIsNone(result)
    