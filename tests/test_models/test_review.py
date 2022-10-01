#!/usr/bin/python3
"""Review mode test
"""
from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class test_review(test_basemodel):
    """Review mode test class
    """

    def __init__(self, *args, **kwargs):
        """Review model test"""
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    # def test_place_id(self):
    #     """Review model test"""
    #     new = self.value()
    #     self.assertEqual(type(new.place_id), str)

    # def test_user_id(self):
    #     """Review model test"""
    #     new = self.value()
    #     self.assertEqual(type(new.user_id), str)

    # def test_text(self):
    #     """Review model test"""
    #     new = self.value()
    #     self.assertEqual(type(new.text), str)
