#!/usr/bin/python3
def remove_char_at(str, n):
    # If n is out of range, return the original string
    if n < 0 or n >= len(str):
        return str
    # Build the new string without the character at position n
    new_str = ""
    for i in range(len(str)):
        if i != n:
            new_str += str[i]
    return new_str
