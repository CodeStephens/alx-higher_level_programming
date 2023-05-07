#!/usr/bin/python3
"""
This Python script fetches the last 10 commits of a repository ("rails") by user ("rails") in GitHub using the GitHub API.

Functions:

get_last_commits():
This function sends a GET request to the GitHub API to retrieve the last 10 commits of a repository by user. It takes two arguments: the repository name and the username of the owner of the repository. It returns the response in JSON format.

Usage:

Run the script using python github_api_commits.py <username> <repository name>, where <username> is the username of the owner of the repository and <repository name> is the name of the repository.
The script will output the SHA of the commit and the name of the author for the last 10 commits of the specified repository by the specified user.

Dependencies:

This script uses the requests package to send HTTP requests to the GitHub API.
This script also uses the sys package to retrieve command-line arguments.

Notes:

This script requires a valid GitHub API token to be set as an environment variable in the user's system.
"""
from requests import get
from sys import argv


if __name__ == "__main__":
    """
    using GitHub API to fetch commit history of a repository
    """

    try:
        url = 'https://api.github.com/repos/{}/{}/commits'.\
                format(argv[2], argv[1])
        response = get(url)
        response_json = response.json()
        for i in range(0, 10):
            print("{}: {}".format(response_json[i].get('sha'),
                                  response_json[i].get('commit').get('author\
                                  ').get('name')))
