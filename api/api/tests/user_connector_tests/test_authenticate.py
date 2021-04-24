import unittest
from unittest.mock import *
from api.database.Database import Database
from api.database.accessors.UserConnector import UserConnector
import datetime

class TestAuthenticate(unittest.TestCase):

  def setUp(self):
    self.username = 'fakeUser'
    self.now = datetime.datetime.now()
    self.timeDiff = 30
    self.validTime = self.now + datetime.timedelta(minutes = self.timeDiff - 1)
    self.invalidTime = self.now + datetime.timedelta(minutes = self.timeDiff + 1)
    
    self.successfulResult = (5, self.username, self.now, self.timeDiff, self.validTime)
    
    self.database = Mock()
    self.database.runSQL.return_value = [self.successfulResult]
    self.user_conn = UserConnector(self.database)

  def test_happy_path(self):
    self.assertEqual(self.user_conn.authenticate('authtoken'), self.username)

  def test_timed_out(self):
    self.database.runSQL.return_value = [(5, self.username, self.now, self.timeDiff, self.invalidTime)]
    self.assertIsNone(self.user_conn.authenticate('authtoken'))

  def test_no_token_entry(self):
    self.database.runSQL.return_value = []
    self.assertIsNone(self.user_conn.authenticate('authtoken'))

  