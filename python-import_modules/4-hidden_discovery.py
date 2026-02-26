#!/usr/bin/python3
import dis

if __name__ == "__main__":
    with open("hidden_4.pyc", "rb") as f:
        f.read(16)  # Skip the header of the .pyc file (magic number + timestamp)
        code_obj = compile(f.read(), "hidden_4.pyc", "exec")
    
    # Get all names defined in the code object
    names = [name for name in code_obj.co_names if not name.startswith("__")]

    # Print names in alpha order
    for name in sorted(names):
        print(name)
