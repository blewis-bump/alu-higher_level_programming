#!/usr/bin/python3
"""Uses GitHub API with Basic Auth to display the user id."""
import requests
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    r = requests.get(
        "https://api.github.com/user",
        auth=(username, password)
    )
    print(r.json().get("id"))
