#!/bin/bash
# Sends a request to 0.0.0.0:5000/catch_me to get a confirmation message.
curl -sL 0.0.0.0:5000/catch_me_3 -X PUT -d "user_id=98" -H "Origin:School"
