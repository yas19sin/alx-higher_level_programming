#!/usr/bin/python3
"""Retrieves the response body from a given URL and displays it."""
from requests import post
from sys import argv


if __name__ == '__main__':

    URL = 'http://0.0.0.0:5000/search_user'
    data = {'q': argv[1] if len(argv) >= 2 else ""}
    response = post(URL, data)

    type_res = response.headers['content-type']

    if type_res == 'application/json':
        result = response.json()
        _id = result.get('id')
        name = result.get('name')
        if (result != {} and _id and name):
            print("[{}] {}".format(_id, name))
        else:
            print('No result')
    else:
        print('Not a valid JSON')
