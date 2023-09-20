#!/usr/bin/python3
""" Unittest for file storage class """

import os
import unittest
from models.base_model import BaseModel
from models.engine.db_storage import DBStorage

models = BaseModel()
storage = DBStorage()


class test_filestorage(unittest.TestCase):
    """ Test cases """

    def setUp(self):
        pass

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_init(self):
        """ Test initialization a privacy of property """
        with self.assertRaises(AttributeError):
            save = storage.__engine
            save = storage.__session

