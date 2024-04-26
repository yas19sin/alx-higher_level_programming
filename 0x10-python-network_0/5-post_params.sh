#!/bin/bash
# POST request with email/subject data
curl -s "$1" -X POST -d 'email=test@gmail.com&subject=I will always be here for PLD' | cat
