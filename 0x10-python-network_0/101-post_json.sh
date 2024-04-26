#!/bin/bash
# Submits a JSON payload via a POST request to the given URL.
curl -s -H "Content-Type: application/json" -d "$1" "$2"
