#!/usr/bin/python3
"""Unittests for console.py"""

import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
import pep8
import models
from models.engine.db_storage import DBStorage


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
        p = pep8.StyleGuide(quiet=True).check_files(["console.py"])
        self.assertEqual(p.total_errors, 0)

    def test_create(self):
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("create")
            self.assertEqual("** class name missing **\n", f.getvalue())

    @unittest.skipIf(type(models.storage) == DBStorage, "Testing DBStorage")
    def test_create_state(self):
        # Create a state
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("create State")
            state_id = f.getvalue().strip()

        # Check if state exist in state list by id
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("all State")
            self.assertIn(state_id, f.getvalue())
