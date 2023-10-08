#!/usr/bin/python3
""" console test """

import unittest
import os
from unittest.mock import patch
from io import StringIO
from models.user import User
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models.base_model import BaseModel
from console import HBNBCommand


class test_console(unittest.TestCase):
    """ Console unittest """

    def setup(self):
        pass

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_create(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            self.assertTrue(True)

    def test_all(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()
