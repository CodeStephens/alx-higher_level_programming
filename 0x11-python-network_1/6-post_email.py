#!/usr/bin/python3
"""
This script sends a POST request to a URL
"""
import requests
from sys import argv


if __name__ == "__main__":

    values_to_post = {'email': argv[2]}
    html_response = requests(argv[1], data=values_to_post)
    print(html_response.text)
