#!/usr/bin/python3
"Displays the 10 most recent commits on a GitHub repository."
import sys
import requests


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits?per_page=10".format(
        sys.argv[2], sys.argv[1])

    r = requests.get(url)
    commits = r.json()
    for commit in commits:
        print("{}: {}".format(
            commit.get("sha"),
            commit.get("commit").get("author").get("name")))
