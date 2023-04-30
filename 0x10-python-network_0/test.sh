#!/bin/bash

url="www.google.com:5000"

# Get the port number from the URL
port=$(echo $url | awk -F: '{print $2}')

# Strip the hostname from the URL
stripped_url=$(echo $url | sed 's/www.google.com//')

# Add the port number back to the stripped URL
stripped_url=${port}

# Print the stripped URL
echo "Stripped URL: $stripped_url"

