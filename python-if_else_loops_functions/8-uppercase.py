#!/usr/bin/python3
def uppercase(str):
    result = ""
    for char in str:
        # Check if char is lowercase letter
        if ord('a') <= ord(char) <= ord('z'):
            # Convert to uppercase by subtracting 32 from ASCII
            result += chr(ord(char) - 32)
        else:
            result += char
    print("{}".format(result))
