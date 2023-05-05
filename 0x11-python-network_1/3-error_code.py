#!/usr/bin/python3
"""
This Python script fetches a URL which displays body of the response
"""
import urllib.request
from sys import argv
from urllib.error import URLError


if __name__ == "__main__":
    req = urllib.request.Request(argv[1])
    try:
        with urllib.request.urlopen(req) as response:
            feedback = response.read()
            print(feedback.decode('utf-8'))
    except URLError as e:
        print('Error code:', e.code)
