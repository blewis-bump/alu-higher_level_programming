#!/usr/bin/python3
"""Module for finding a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    """Find a peak in a list of unsorted integers using binary search.

    A peak is defined as an element that is greater than or equal to
    its neighbors. Uses binary search for O(log(n)) complexity.

    Args:
        list_of_integers: A list of unsorted integers.

    Returns:
        A peak integer from the list, or None if the list is empty.
    """
    if not list_of_integers:
        return None

    lo = 0
    hi = len(list_of_integers) - 1

    while lo < hi:
        mid = (lo + hi) // 2
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            lo = mid + 1
        else:
            hi = mid

    return list_of_integers[lo]
