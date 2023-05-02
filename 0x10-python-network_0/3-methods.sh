#!/bin/bash
# Send DELETE request and display response body
curl -sIX OPTIONS $1 | grep 'Allow:' | cut -d ' ' -f 2-
