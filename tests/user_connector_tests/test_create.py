import unittest
from unittest.mock import *
from database.Database import Database
from database.accessors.UserConnector import UserConnector
import datetime

class TestCreate(unittest.TestCase):

  def setUp(self):
    self.database = Mock()
    self.user_conn = UserConnector(self.database)

  def test_happy_path(self):
    pass
  