#!/usr/bin/python3
"""Lists the 10 most recent commits of a GitHub repository."""
import requests
import sys


if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(owner, repo)
    r = requests.get(url)
    commits = r.json()
    for commit in commits[:10]:
        sha = commit.get("sha")
        name = commit.get("commit").get("author").get("name")
        print("{}: {}".format(sha, name))
