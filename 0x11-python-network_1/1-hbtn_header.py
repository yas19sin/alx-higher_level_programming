#!/usr/bin/python3
"""
Displays the value of the X-Request-Id HTTP header,
which is used to identify a request.
"""


if __name__ == "__main__":
    import sys
    import urllib.request

    with urllib.request.urlopen(sys.argv[1]) as response:
        print(response.headers["X-Request-Id"])
