#!/bin/bash
# List all HTTP methods a server at the given URL will respond to.
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
