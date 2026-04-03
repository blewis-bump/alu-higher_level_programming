#!/usr/bin/python3
"""Unittest for Square class."""
import unittest
import os
from io import StringIO
from unittest.mock import patch
from models.base import Base
from models.square import Square


class TestSquare(unittest.TestCase):
    """Tests for the Square class."""

    def setUp(self):
        """Reset __nb_objects before each test."""
        Base._Base__nb_objects = 0

    def test_basic_creation(self):
        """Test basic square creation."""
        s = Square(5)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)

    def test_id_auto(self):
        """Test auto id."""
        s = Square(5)
        self.assertEqual(s.id, 1)

    def test_id_manual(self):
        """Test manual id."""
        s = Square(5, 0, 0, 12)
        self.assertEqual(s.id, 12)

    def test_size_setter(self):
        """Test size setter."""
        s = Square(5)
        s.size = 10
        self.assertEqual(s.size, 10)
        self.assertEqual(s.width, 10)
        self.assertEqual(s.height, 10)

    def test_size_type_error(self):
        """Test size type error."""
        with self.assertRaises(TypeError) as e:
            Square("9")
        self.assertEqual(str(e.exception), "width must be an integer")

    def test_size_value_error(self):
        """Test size value error."""
        with self.assertRaises(ValueError) as e:
            Square(-1)
        self.assertEqual(str(e.exception), "width must be > 0")

    def test_x_type_error(self):
        """Test x type error."""
        with self.assertRaises(TypeError):
            Square(5, "1")

    def test_y_type_error(self):
        """Test y type error."""
        with self.assertRaises(TypeError):
            Square(5, 0, "1")

    def test_area(self):
        """Test area method."""
        s = Square(5)
        self.assertEqual(s.area(), 25)

    def test_str(self):
        """Test __str__ method."""
        s = Square(5, 1, 3, 10)
        self.assertEqual(str(s), "[Square] (10) 1/3 - 5")

    def test_display_no_x_y(self):
        """Test display without x and y."""
        s = Square(3)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            s.display()
            self.assertEqual(fake_out.getvalue(), "###\n###\n###\n")

    def test_display_no_y(self):
        """Test display without y (x set)."""
        s = Square(2, 1)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            s.display()
            self.assertEqual(fake_out.getvalue(), " ##\n ##\n")

    def test_display_with_x_and_y(self):
        """Test display with x and y."""
        s = Square(2, 1, 2)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            s.display()
            self.assertEqual(fake_out.getvalue(), "\n\n ##\n ##\n")

    def test_update_args(self):
        """Test update with positional args."""
        s = Square(5)
        s.update(10, 2, 3, 4)
        self.assertEqual(s.id, 10)
        self.assertEqual(s.size, 2)
        self.assertEqual(s.x, 3)
        self.assertEqual(s.y, 4)

    def test_update_kwargs(self):
        """Test update with keyword args."""
        s = Square(5)
        s.update(size=7, y=1, id=89)
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 7)
        self.assertEqual(s.y, 1)

    def test_to_dictionary(self):
        """Test to_dictionary method."""
        s = Square(10, 2, 1)
        d = s.to_dictionary()
        self.assertIsInstance(d, dict)
        self.assertEqual(d['size'], 10)
        self.assertEqual(d['x'], 2)
        self.assertEqual(d['y'], 1)
        self.assertIn('id', d)

    def test_create(self):
        """Test create class method."""
        s1 = Square(5, 2, 3)
        s1_dict = s1.to_dictionary()
        s2 = Square.create(**s1_dict)
        self.assertEqual(str(s1), str(s2))
        self.assertFalse(s1 is s2)

    def test_size_zero(self):
        """Test size zero raises ValueError."""
        with self.assertRaises(ValueError):
            Square(0)

    def test_x_value_error(self):
        """Test x negative raises ValueError."""
        with self.assertRaises(ValueError):
            Square(5, -1)

    def test_y_value_error(self):
        """Test y negative raises ValueError."""
        with self.assertRaises(ValueError):
            Square(5, 0, -1)

    def test_save_to_file_none(self):
        """Test Square.save_to_file(None)."""
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")
        os.remove("Square.json")

    def test_save_to_file_empty(self):
        """Test Square.save_to_file([])."""
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")
        os.remove("Square.json")

    def test_save_to_file_one_square(self):
        """Test Square.save_to_file([Square(1)])."""
        Square.save_to_file([Square(1)])
        with open("Square.json", "r") as f:
            content = f.read()
        self.assertIn("size", content)
        os.remove("Square.json")

    def test_load_from_file_no_file(self):
        """Test Square.load_from_file() when file does not exist."""
        if os.path.exists("Square.json"):
            os.remove("Square.json")
        result = Square.load_from_file()
        self.assertEqual(result, [])

    def test_load_from_file_exists(self):
        """Test Square.load_from_file() when file exists."""
        s1 = Square(5, 2, 3)
        Square.save_to_file([s1])
        result = Square.load_from_file()
        self.assertEqual(len(result), 1)
        self.assertIsInstance(result[0], Square)
        self.assertEqual(result[0].size, 5)
        os.remove("Square.json")


if __name__ == '__main__':
    unittest.main()
