#!/usr/bin/python3
import marshal

if __name__ == "__main__":
    with open("hidden_4.pyc", "rb") as f:
        f.read(16)  # skip header (Python 3.8)
        code_obj = marshal.load(f)  # read the code object

    # get all names in the code object that do not start with __
    names = [name for name in code_obj.co_names if not name.startswith("__")]

    # print names in alphabetical order
    for name in sorted(names):
        print(name)
