#!/usr/bin/python3
""" Unittest for file storage class """

import os
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

models = BaseModel()
storage = FileStorage()


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
            save = storage.__file_path
            save = storage.___objects

    def test_all(self):
        """ Test for all() """
        self.assertIsInstance(storage.all(), dict)

    def test_new(self):
        """ Test new() """
        storage.new(models)
        self.assertTrue(storage.all())  # check if empty

    def test_save(self):
        storage.save()
        filename = "file.json"
        self.assertTrue(os.path.exists(filename))

    def test_reload(self):
        all_objs = storage.all()
        for obj_id in all_objs.keys():
            obj = all_objs[obj_id]
            self.assertIsInstance(obj, object)
