#!/bin/bash
# This script attempts to print out the content of the url its trying to reach
[ echo $(curl -s  -w '%{http_code}' -o /dev/null $1) -eq 200 ] && echo $(curl -L $1) || echo '' 
