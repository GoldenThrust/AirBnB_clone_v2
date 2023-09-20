#!/usr/bin/python3
import unittest
""" Unitest for Amenity class """

from models.amenity import Amenity
models = Amenity()


class test_amenity(unittest.TestCase):
    """ test cases """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_init(self):
        models.name = "Adeniji"
        self.assertIsNotNone(models.id)
        self.assertTrue(models.name)


if __name__ == "__main__":
    unittest.main()
