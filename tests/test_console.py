#!/usr/bin/python3
"""Unittests for console.py"""

import unittest


class TestHBNBCommand(unittest.TestCase):
    """Test HBNB console"""

        def test_emptyline(self):
        """Test empty line input."""
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("\n")
            self.assertEqual("", f.getvalue())
