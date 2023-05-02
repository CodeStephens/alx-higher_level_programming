#!/bin/bash
# HTTP request POST method on JSON payload
curl -sL -X PUT "0.0.0.0:5000/catch_me" -H "Origin: X-School" -d "User-Id=98"
