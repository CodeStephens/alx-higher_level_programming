#!/bin/bash
# This script attempts to get the download size of the url its trying to reach
echo "$(curl -s -w '%{size_download}' -o /dev/null $1)"
