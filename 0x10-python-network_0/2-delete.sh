#!/bin/bash
# Send a DELETE request to the given URL and display the server's response.
curl --silent --location --request DELETE "$1" | cat
