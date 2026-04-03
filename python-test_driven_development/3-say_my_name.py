#!/usr/bin/python3
"""Module for printing a name."""


def say_my_name(first_name, last_name=""):
    """Print My name is <first_name> <last_name>.

    Args:
        first_name: first name string
        last_name: last name string (default empty)
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
