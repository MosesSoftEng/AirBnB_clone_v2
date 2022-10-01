#!/usr/bin/python3
"""State model tests
"""
from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """State model test"""

    def __init__(self, *args, **kwargs):
        """State model test"""
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    # def test_name3(self):
    #     """State model test"""
    #     new = self.value()
    #     self.assertEqual(type(new.name), str)
