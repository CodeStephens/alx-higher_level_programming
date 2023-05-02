#!/bin/bash
# HTTP request POST method on JSON payload
curl -s $1 -d "@$2" -X POST -H 'Content-Type: application/json'
