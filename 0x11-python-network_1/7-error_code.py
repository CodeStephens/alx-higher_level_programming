#!/usr/bin/python3
"""
This Python script fetches a URL which displays body of the response
"""
import requests
from sys import argv


if __name__ == "__main__":
    html_response = requests.get(argv[1])
    if html_response.status_code >= 400:
        print("Error code:{}".format(html_response.status_code))
    else:
        print(html_response.text)
