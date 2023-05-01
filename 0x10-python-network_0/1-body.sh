#!/bin/bash
# This script attempts to print out the content of the url its trying to reach
if [ $(curl -s -o /dev/null -w "%{http_code}" "$1") -eq "200" ]; then echo "$(curl -s $1)"; else echo ""; fi 
