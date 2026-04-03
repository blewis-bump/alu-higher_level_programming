#!/usr/bin/python3
"""Module for printing a square."""


def print_square(size):
    """Print a square with the character #.

    Args:
        size: size length of the square (integer)
    """
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
