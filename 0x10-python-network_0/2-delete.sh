#!/bin/bash
# Send DELETE request and display response body
curl -X DELETE -i $1 | grep -v "^HTTP" | sed -e "1,/^\s*$/d"
