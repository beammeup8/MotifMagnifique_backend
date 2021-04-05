from os import urandom
from api.utilities import data_format_functions as dff
import bcrypt
from api.database.Database import Database
from datetime import timedelta
from base64 import b64encode
import sys
import os
from .UserConnector import UserConnector
curr_dir = os.getcwd()
sys.path.append(curr_dir)


class PatternConnector:
    def __init__(self, dbCon, userConnector):
        self.dbCon = dbCon
        self.table = "pattern"
        self.userConnector = userConnector

    
