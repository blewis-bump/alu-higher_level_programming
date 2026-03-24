#!/usr/bin/python3
"""Module defining MyList, a list subclass with a sorted print method."""


class MyList(list):
    """A class that inherits from list and adds a sorted print method."""

    def print_sorted(self):
        """Print the list elements sorted in ascending order."""
        print(sorted(self))
