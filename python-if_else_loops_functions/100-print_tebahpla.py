#!/usr/bin/python3
for i in range(25, -1, -1):
    if (25 - i) % 2 == 0:
        c = chr(ord('a') + i)
    else:
        c = chr(ord('A') + i)
    print("{}".format(c), end="")
