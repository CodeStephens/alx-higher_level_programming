#!/bin/bash
# Displays just the status code
curl -s $1 -o /dev/null -w '%{http_code}'
