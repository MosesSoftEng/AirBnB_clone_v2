#!/usr/bin/python3
"""Review mode test
"""
from tests.test_models.test_base_model import test_basemodel
from models.review import Review
import pep8


class test_review(test_basemodel):
    """Review mode test class
    """

    def __init__(self, *args, **kwargs):
        """Review model test"""
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """Review model test"""
        new = self.value(place_id="52463d70-b0e3-4edd-b1fb-5f33d7d12947")
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """Review model test"""
        new = self.value(user_id="cbbc0259-4e45-447c-9139-887c4873b2f6")
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """Review model test"""
        new = self.value(text="Excepteur sint occaecat cupidatat non proident")
        self.assertEqual(type(new.text), str)

    def test_pep8(self):
        """Check pep8 styling"""
        p = pep8.StyleGuide(quiet=True).check_files(["models/review.py"])
        self.assertEqual(p.total_errors, 0)
