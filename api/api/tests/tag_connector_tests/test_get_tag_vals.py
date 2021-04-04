import unittest
from unittest.mock import *
from api.database.Database import Database
from api.database.accessors.TagConnector import TagConnector
import datetime


class TestGetTagVals(unittest.TestCase):

    def setUp(self):
      self.name = 'test'
      

      self.successfulResult = [(5, 'test'), ]
      self.unsucessfulResult = [(),]
      self.database = Mock()

      self.tag_conn = TagConnector(self.database)

    def test_happy_path_exists(self):
      self.database.runSQL.return_value = self.successfulResult
      self.assertEqual(self.tag_conn.getTagVals(
          self.name, ), self.successfulResult)

    def test_happy_path_not_exists(self):
      self.database.runSQL.side_effect = [(),]
      self.assertEqual(self.tag_conn.getTagVals(
        self.name, ), self.unsucessfulResult)
