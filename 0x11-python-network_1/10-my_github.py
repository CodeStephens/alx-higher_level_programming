#!/usr/bin/python3
"""
This python script fetches GitHub id using GitHub API via GitHub
authentication credentials (password and username)
"""
import requests
from sys import argv


if __name__ == '__main_':
    url = 'https://api.github.com/user'
    username = argv[1]
    password = argv[2]
    response = requests.get(url, auth=auth.HTTPBasicAuth(username, password))
    print(response)
    print(response.json().get('id'))
