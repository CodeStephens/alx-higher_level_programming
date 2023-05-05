#!/usr/bin/python3
"""
This Python script sends a request to a URL and fetches the value of
'X-Request-Id' in the header
"""
import urllib.request
from sys import argv


if __name__ == "__main__":

    with urllib.request.urlopen(argv[1]) as response:
        html = response.info()
        print(html.get('X-Request-Id'))
