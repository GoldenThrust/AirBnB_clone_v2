#!/usr/bin/python3
""" Module for testing file storage"""
import unittest
from models.base_model import BaseModel
from models import storage
import os


class test_fileStorage(unittest.TestCase):
    """ Class to test the file storage method """

    def setUp(self):
        """ Set up test environment """
        del_list = []
        for key in storage.all.Keys():
            del_list.append(key)
        for key in del_list:
            del storage.all()[key]

    def tearDown(self):
        pass

    def test_obj_list_empty(self):
        """ __objects is initially empty """
        self.assertEqual(len(storage.all()), 0)

    def test_new(self):
        """ New object is correctly added to __objects """
        new = BaseModel()
        for obj in storage.all().values():
            temp = obj
        self.assertTrue(temp is obj)

    def test_all(self):
        """ __objects is properly returned """
        new = BaseModel()
        temp = storage.all()
        self.assertIsInstance(temp, dict)

    def test_save(self):
        """ FileStorage save method """
        new = BaseModel()
        storage.save()
        self.assertTrue(True)

    def test_reload(self):
        """ Storage file is successfully loaded to __objects """
        new = BaseModel()
        storage.save()
        storage.reload()
        for obj in storage.all().values():
            loaded = obj
        self.assertEqual(new.to_dict()['id'], loaded.to_dict()['id'])

    def test_reload_empty(self):
        """ Load from an empty file """
        with open('file.json', 'w') as f:
            pass
        with self.assertRaises(ValueError):
            storage.reload()

    def test_reload_from_nonexistent(self):
        """ Nothing happens if file does not exist """
        self.assertEqual(storage.reload(), None)

    def test_type_objects(self):
        """ Confirm __objects is a dict """
        self.assertEqual(type(storage.all()), dict)

    def test_key_format(self):
        """ Key is properly formatted """
        new = BaseModel()
        _id = new.to_dict()['id']
        for key in storage.all().keys():
            temp = key
        self.assertEqual(temp, 'BaseModel' + '.' + _id)

    def test_storage_var_created(self):
        """ FileStorage object storage created """
        from models.engine.db_storage import DBStorage
        print(type(storage))
        self.assertEqual(type(storage), DBStorage)
