#!/bin/bash
# take a URL, send a request to that URL, and display size of the body of the response.
# Usage: ./0-body_size.sh 0.0.0.0:5000
curl -s "${1}" | wc -c
