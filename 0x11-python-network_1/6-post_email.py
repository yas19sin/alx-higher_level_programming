"""A script that retrieves and displays the value of the X-Request-Id
header variable when sending a request to a URL.
"""
from sys
from urllib.request

if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))