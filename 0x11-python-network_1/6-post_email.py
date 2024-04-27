"""A script that retrieves and displays the value of the X-Request-Id
header variable when sending a request to a URL.
"""
from sys import argv
from requests import post

if __name__ == "__main__":
    url = argv[1]
    email = argv[2]
    res = post(url, {'email': email})
    print(res.text)
