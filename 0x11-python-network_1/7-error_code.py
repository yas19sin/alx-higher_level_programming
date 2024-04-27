#!/usr/bin/python3
"""Retrieves and displays the body of a webpage by sending a request
to a given URL.
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    r = requests.get(url, stream=True)
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        for line in r.iter_lines():
            if line:
                print(line.decode('utf-8'))
