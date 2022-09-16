#!/usr/bin/python3
"""Unittests for console.py"""

import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


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
