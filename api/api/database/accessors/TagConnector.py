from os import urandom
from api.utilities import data_format_functions as dff
import bcrypt
from api.database.Database import Database
from datetime import timedelta
from base64 import b64encode
import sys
import os
curr_dir = os.getcwd()
sys.path.append(curr_dir)


class TagConnector:
    def __init__(self, dbCon):
        self.dbCon = dbCon
        self.table = "tag"

    # gets tag ID based on the name (which must be unique)

    def getCreateTag(self, name, value):
        query = "select id from tag where name=? and value=?"
        res = self.dbCon.runSQL(query, (name, value))

        if len(res) == 0:
            completed = self.dbCon.insertInto(
                self.table, ["name", "value"], (name, value))
            if completed:
                res = self.dbCon.runSQL(query, (name, value))
            else:
                return None

        return res[0][0]

    def getTagVals(self, name):
        query = "select id, value from tag where name=?"
        re = self.dbCon.runSQL(query, (name, ))

        if len(re) == 0:
            return [(), ]
        return re
