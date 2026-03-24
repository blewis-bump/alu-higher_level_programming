#!/usr/bin/python3
"""Module that defines BaseGeometry with area and integer_validator methods."""


class BaseGeometry:
    """A base class for geometry with validation and area methods."""

    def area(self):
        """Raise an Exception indicating area is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that value is a positive integer, raise errors if not."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
