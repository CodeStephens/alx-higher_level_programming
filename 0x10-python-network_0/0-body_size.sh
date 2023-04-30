#!/bin/bash
# This script attempts to take a (URL) argument; while a URL is sent to the argument, the size of the content in bytes is sought for

if [ -z "$1" ]; then
	echo "please enter a valid url"
	exit 1
fi

port=$(echo "$1" | awk -F: '{print $2}')
if [ $port = "5000" ]; then
	size_of_download=$(curl -s -w '%{size_download}' -o /dev/null $1)
	echo ${size_of_download}
fi
