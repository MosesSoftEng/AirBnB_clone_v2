#!/usr/bin/python3
"""Place model test"""
from tests.test_models.test_base_model import test_basemodel
from models.place import Place
import pep8


class test_Place(test_basemodel):
    """Place model test"""

    def __init__(self, *args, **kwargs):
        """Place model test"""
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """Place model test"""
        new = self.value(city_id="test_id")
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """Place model test"""
        new = self.value(user_id="test_id")
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """Place model test"""
        new = self.value(name="test_name")
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """Place model test"""
        new = self.value(description="test description")
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """Place model test"""
        new = self.value(number_rooms=10)
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """Place model test"""
        new = self.value(number_bathrooms=1)
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """Place model test"""
        new = self.value(max_guest=10)
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """Place model test"""
        new = self.value(price_by_night=100)
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """Place model test"""
        new = self.value(latitude=17.08)
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """Place model test"""
        new = self.value(latitude=1.977)
        self.assertEqual(type(new.latitude), float)

    def test_amenity_ids(self):
        """Place model test"""
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)

    def test_pep8(self):
        """Check pep8 styling"""
        p = pep8.StyleGuide(quiet=True).check_files(["models/place.py"])
        self.assertEqual(p.total_errors, 0)
