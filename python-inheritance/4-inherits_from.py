#!/usr/bin/python3
"""Module providing a function to check strict inheritance from a class."""


def inherits_from(obj, a_class):
    """Return True if obj is an instance of a subclass of a_class only."""
    return isinstance(obj, a_class) and type(obj) is not a_class
