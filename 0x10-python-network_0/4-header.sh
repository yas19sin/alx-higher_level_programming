#!/bin/bash
# Send a GET request with a custom header variable to a given URL.
curl -s "$1" -H "X-School-User-Id: 98"
