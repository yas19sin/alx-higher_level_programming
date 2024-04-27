#!/usr/bin/python3
"""
Logs into GitHub and retrieves your user ID using the GitHub API
"""
from sys import argv
from requests import Session

if __name__ == '__main__':

    username = argv[1]
    password = argv[2]

    with Session() as s:
        s.auth = (username, password)
        response = s.get("https://api.github.com/user")

    json = response.json()
    print(json.get('id'))
