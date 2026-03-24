#!/usr/bin/python3
"""Module that defines a Square with custom string representation."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class representing a square with a [Square] string description."""

    def __init__(self, size):
        """Initialize a Square with a validated private size."""
        self.integer_validator('size', size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2

    def __str__(self):
        """Return the string description of the square."""
        return '[Square] {}/{}'.format(self.__size, self.__size)
