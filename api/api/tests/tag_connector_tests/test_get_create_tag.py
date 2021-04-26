import unittest
from unittest.mock import *
from api.database.Database import Database
from api.database.accessors.TagConnector import TagConnector
import datetime

class TestGetCreateTag(unittest.TestCase):

  def setUp(self):
    self.name = 'tagName'
    self.value = 'tagVal'
    
    self.successfulResult = 5
    self.database = Mock()

    self.tag_conn = TagConnector(self.database)

  def test_happy_path_exists(self):
    self.database.runSQL.return_value = [(self.successfulResult, )]
    self.assertEqual(self.tag_conn.getCreateTag(self.name, self.value), self.successfulResult)

  def test_sad_path_not_exists(self):
    self.database.runSQL.side_effect = [[], [(self.successfulResult, )]]
    self.database.insertInto.return_value = True
    self.assertEqual(self.tag_conn.getCreateTag(self.name, self.value), self.successfulResult)

  def test_sad_path_create_fail(self):
    self.database.runSQL.return_value = []
    self.database.insertInto.return_value = False
    self.assertEqual(self.tag_conn.getCreateTag(self.name, self.value), None)
    
  