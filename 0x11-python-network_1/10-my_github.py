#!/usr/bin/python3
"""
This python scripts intend to retrieve GitHud id via GitHub API using
GitHub credentials (username and password) as command line argument to
authenticate
"""
import requests
from sys import argv


# Get GitHub credentials from command line arguments
username = argv[1]
password = argv[2]

# Set up the API endpoint and headers
url = 'https://api.github.com/user'
headers = {'Accept': 'application/vnd.github.v3+json'}

# Make the API request using Basic Authentication
response = requests.get(url, auth=(username, password), headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # Print the user ID
    user_id = response.json()['id']
    print(f"Your user ID is: {user_id}")
else:
    print("Failed to get user ID. Check your credentials and try again.")
