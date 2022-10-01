#!/usr/bin/python3
"""User model unit test module"""
from tests.test_models.test_base_model import test_basemodel
from models.user import User
import pep8


class test_User(test_basemodel):
    """User model unit test class"""

    def __init__(self, *args, **kwargs):
        """User model test"""
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """User model test"""
        new = self.value(first_name='John')
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """User model test"""
        new = self.value(last_name='Doe')
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """User model test"""
        new = self.value(email='john@mail.com')
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """User model test"""
        new = self.value(password='qNCLmXj8kPbNrAVQd2s1')
        self.assertEqual(type(new.password), str)

    def test_pep8(self):
        """Check pep8 styling"""
        p = pep8.StyleGuide(quiet=True).check_files(["models/user.py"])
        self.assertEqual(p.total_errors, 0)
