#!/usr/bin/python3
"""
This Python script fetches the last 10 commits of a repository ("rails") by
user ("rails") in GitHub using the GitHub API.
"""
from requests import get
from sys import argv


if __name__ == "__main__":
    """
    using GitHub API to fetch commit history of a repository
    """

    url = 'https://api.github.com/repos/{}/{}/commits'.format(argv[2], argv[1])
    response = get(url)
    lenOfCommits = len(response.json())
    commits = response.json()
    for i in range(0, lenOfCommits):
        print("{}: {}".format(commits[i].get('sha'), commits[i].get('commit').
                              get('author').get('name')))
