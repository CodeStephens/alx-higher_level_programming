#!/usr/bin/python3
"""
This python script displays the last 10 commits of a repository (rails) by
user (rails) in Github using GitHub API
"""
from requests import get
from sys import argv


if __name__ == "__main__":
    """ using GitHub API to fetch commit history of a repository """
    try:
        url = 'https://api.github.com/repos/{}/{}/commits'.\
                format(argv[2], argv[1])
        response = get(url)
        response_json = response.json()
        for i in range(0, 10):
            print("{}: {}".format(response_json[i].get('sha'),
                                  response_json[i].get('commit').get('author\
                                  ').get('name')))
