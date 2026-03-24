#!/usr/bin/python3
"""Module that defines BaseGeometry with an unimplemented area method."""


class BaseGeometry:
    """A base class for geometry with an area method that raises Exception."""

    def area(self):
        """Raise an Exception indicating area is not implemented."""
        raise Exception("area() is not implemented")
