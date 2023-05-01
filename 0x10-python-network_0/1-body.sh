#!/bin/bash
# This script attempts to print out the content of the url its trying to reach
echo "$(curl -s -L "$1")"
