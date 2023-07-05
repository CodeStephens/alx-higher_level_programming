#!/usr/bin/python3
"""
This python script fetches GitHub id using GitHub API via GitHub
authentication credentials (password and username)
"""
import requests
from sys import argv
from requests import auth


if __name__ == '__main__':
    url = 'https://api.github.com/user'
    headers = {'Accept': 'application/vnd.github.v3+json'}
    username = argv[1]
    password = argv[2]
    response = requests.get(url, auth=auth.HTTPBasicAuth(username, password),\
            headers=headers)
    print(response.json().get('id'))
