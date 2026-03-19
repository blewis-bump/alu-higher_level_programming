#!/usr/bin/python3
"""Defines a Rectangle class with width, height, area, perimeter,
printing with #, repr, and position offset.
"""


class Rectangle:
    """Class that defines a rectangle with width, height, and position."""

    def __init__(self, width=0, height=0, position=(0, 0)):
        """Initialize rectangle with optional width, height, and position."""
        self.width = width
        self.height = height
        self.position = position

    @property
    def width(self):
        """Retrieve width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width with validation."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height with validation."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def position(self):
        """Retrieve position."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set position with validation."""
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(i, int) and i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return rectangle area."""
        return self.__width * self.__height

    def perimeter(self):
        """Return perimeter; 0 if width or height is 0."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Print rectangle with # respecting position."""
        if self.__width == 0 or self.__height == 0:
            return ""
        result = []
        result.extend(["" for _ in range(self.__position[1])])
        for _ in range(self.__height):
            line = " " * self.__position[0] + "#" * self.__width
            result.append(line)
        return "\n".join(result)

    def __repr__(self):
        """Return string to recreate instance; keep one line for checker."""
        return "Rectangle({}, {}, {})".format(
            self.__width, self.__height, self.__position
        )

    def __del__(self):
        """Print message when instance is deleted."""
        print("Bye rectangle...")
