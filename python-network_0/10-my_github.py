#!/usr/bin/python3
"""Script that takes GitHub credentials and uses the GitHub API to display the id."""
import sys
import requests


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    url = "https://api.github.com/user"
    r = requests.get(url, auth=(username, password))
    try:
        print(r.json().get("id"))
    except Exception:
        print("None")
