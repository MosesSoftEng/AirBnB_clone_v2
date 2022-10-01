#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class test_Amenity(test_basemodel):
    """
    Tests for Amemnity class instances.
    """
    def __init__(self, *args, **kwargs):
        """
        Constructor to setup test parameters
        """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """
        Test if name is of type string
        """
        new = self.value(name=self.name)
        self.assertEqual(type(new.name), str)
