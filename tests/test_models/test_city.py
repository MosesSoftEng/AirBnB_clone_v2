#!/usr/bin/python3
"""
City unit test
"""
from tests.test_models.test_base_model import test_basemodel
from models.city import City
import pep8


class test_City(test_basemodel):
    """
    Tests for City class instances.
    """

    def __init__(self, *args, **kwargs):
        """
        Constructor set initial values
        """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """
        Tes if city state_id is of type string
        """
        new = self.value(name=self.name, state_id='test_id')
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """
        Test if city name is of type string
        """
        new = self.value(name=self.name)
        self.assertEqual(type(new.name), str)

    def test_pep8(self):
        """Check pep8 styling"""
        p = pep8.StyleGuide(quiet=True).check_files(["models/city.py"])
        self.assertEqual(p.total_errors, 0)
