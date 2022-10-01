#!/usr/bin/python3
"""State model tests
"""
from tests.test_models.test_base_model import test_basemodel
from models.state import State
import pep8


class test_state(test_basemodel):
    """State model tests"""

    def __init__(self, *args, **kwargs):
        """State model test"""
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """State model test"""
        new = self.value(name="Texas")
        self.assertEqual(type(new.name), str)

    def test_pep8(self):
        """Check pep8 styling"""
        p = pep8.StyleGuide(quiet=True).check_files(["models/state.py"])
        self.assertEqual(p.total_errors, 0)
