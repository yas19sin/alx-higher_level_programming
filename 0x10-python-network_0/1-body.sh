#!/bin/bash
# Fetch and display the response body for successful (200) requests to a URL.
# Usage: ./1-body.sh 0.0.0.0:5000/route_1 ; echo ""
curl --silent --location --request GET "$1" | cat
