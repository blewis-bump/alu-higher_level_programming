#!/usr/bin/python3
for i in range(25, -1, -1):
    c = chr(ord('a') + i) if i % 2 == 0 else chr(ord('A') + i)
    print("{}".format(c), end="")
