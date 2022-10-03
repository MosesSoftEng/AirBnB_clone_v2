#!/usr/bin/python3
"""Unittests for console.py"""

import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
import pep8


class TestHBNBCommand(unittest.TestCase):
    """Test HBNB console"""

    @classmethod
    def setUpClass(cls):
        """HBNBCommand testing setup"""
        cls.HBNB = HBNBCommand()

    def test_emptyline(self):
        """Test empty line input."""
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("\n")
            self.assertEqual("", f.getvalue())

    def test_pep8(self):
        """Check pep8 styling"""
        p = pep8.StyleGuide(quiet=True).check_files(["models/user.py"])
        self.assertEqual(p.total_errors, 0)
