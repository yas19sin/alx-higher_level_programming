#!/bin/bash
# Request a URL and print the HTTP status code of the response.
curl -sL -o /dev/null -w "%{http_code}" "$1"
