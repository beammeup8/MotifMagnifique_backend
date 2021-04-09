import unittest
from unittest.mock import *
from ...database.Database import Database
from ...database.accessors.UserConnector import UserConnector
from ...database.accessors import UserConnector as uc
import datetime

class TestCheckPassword(unittest.TestCase):

  def setUp(self):
    self.successfulResult = (5,)
    self.salt = b'$2b$12$mwSIOyxLJid1jFLgnU0s0.'
    self.database = Mock()
    self.database.runSQL.return_value = [self.successfulResult]
    self.user_conn = UserConnector(self.database)
    uc.hashPassword = MagicMock(return_value = (self.salt, "some hashed password"))

  def test_happy_path(self):
    uc.hashPassword.return_value = (self.salt, "some hashed password")
    self.assertIsNotNone(self.user_conn.checkPassword('some user', 'some password', self.salt))

  def test_wrong_password_or_username(self):
    self.database.runSQL.return_value = []
    self.assertIsNone(self.user_conn.checkPassword('some user', 'some password', self.salt))

  def test_multiple_results(self):
    self.database.runSQL.return_value = [self.successfulResult, self.successfulResult]
    self.assertIsNone(self.user_conn.checkPassword('some user', 'some password', self.salt))
