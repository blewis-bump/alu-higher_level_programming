#!/usr/bin/python3
"""Unittest for Base class."""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Tests for the Base class."""

    def setUp(self):
        """Reset __nb_objects before each test."""
        Base._Base__nb_objects = 0

    def test_auto_id(self):
        """Test auto id assignment."""
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)

    def test_manual_id(self):
        """Test manual id assignment."""
        b = Base(12)
        self.assertEqual(b.id, 12)

    def test_mixed_id(self):
        """Test mixed id assignment."""
        b1 = Base()
        b2 = Base(12)
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 12)
        self.assertEqual(b3.id, 2)

    def test_to_json_string_normal(self):
        """Test to_json_string with normal input."""
        d = [{'id': 1, 'width': 10}]
        result = Base.to_json_string(d)
        self.assertIsInstance(result, str)
        self.assertIn('"id": 1', result)

    def test_to_json_string_empty(self):
        """Test to_json_string with empty list."""
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_none(self):
        """Test to_json_string with None."""
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_from_json_string_normal(self):
        """Test from_json_string with normal input."""
        s = '[{"id": 1, "width": 10}]'
        result = Base.from_json_string(s)
        self.assertIsInstance(result, list)
        self.assertEqual(result[0]['id'], 1)

    def test_from_json_string_empty(self):
        """Test from_json_string with empty string."""
        self.assertEqual(Base.from_json_string("[]"), [])

    def test_from_json_string_none(self):
        """Test from_json_string with None."""
        self.assertEqual(Base.from_json_string(None), [])

    def test_id_zero(self):
        """Test id with zero."""
        b = Base(0)
        self.assertEqual(b.id, 0)

    def test_id_negative(self):
        """Test id with negative value."""
        b = Base(-5)
        self.assertEqual(b.id, -5)


if __name__ == '__main__':
    unittest.main()
