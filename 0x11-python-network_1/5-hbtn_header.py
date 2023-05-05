#!/usr/bin/python3
"""
This Python script takes in a URL, sends a request to the URL, and
displays the value of the variable X-Request-Id in the response header
using only requests and sys
"""
import requests
from sys import argv


if __name__ == "__main__":
    response = requests.get(argv[1])
    x_request_id = response.headers.get('X-Request-Id')
    print(x_request_id)
