#!/usr/bin/python3
"""Module that defines a Square class inheriting from Rectangle."""
Rectangle = __import__(9-rectangle).Rectangle


class Square(Rectangle):
    """A class that represents a square, inheriting from Rectangle."""

    def __init__(self, size):
        """Initialize a Square with a validated private size."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2
