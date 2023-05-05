#!/usr/bin/python3
"""
This script sends a POST request to a URL
"""
import urllib.request
from sys import argv


if __name__ == "__main__":

    values_to_post = {'email': argv[2]}
    encoding_values = urllib.parse.urlencode(values_to_post).encode('ascii')
    data_to_post = urllib.request.Request(argv[1], encoding_values)
    with urllib.request.urlopen(data_to_post) as response:
        html = response.read()
        print(html.decode('utf-8'))
