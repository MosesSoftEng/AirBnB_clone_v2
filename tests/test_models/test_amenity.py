#!/usr/bin/python3
"""
Amenty test class
"""
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity
import pep8
from models.engine.db_storage import DBStorage
import unittest
import models


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

    def test_pep8(self):
        """Check pep8 styling"""
        p = pep8.StyleGuide(quiet=True).check_files(["models/amenity.py"])
        self.assertEqual(p.total_errors, 0)

    @unittest.skipIf(type(models.storage) == DBStorage, "Testing DBStorage")
    def test_save(self):
        """Test save method with FileStorage."""
        new_amenity = self.value(name=self.name)
        self.assertNotEqual(new_amenity.created_at, new_amenity.updated_at)
