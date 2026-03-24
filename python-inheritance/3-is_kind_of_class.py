#!/usr/bin/python3
"""Module that provides a function to check instance or inherited class."""


def is_kind_of_class(obj, a_class):
    """Return True if obj is an instance of a_class or inherits from it."""
    return isinstance(obj, a_class)
