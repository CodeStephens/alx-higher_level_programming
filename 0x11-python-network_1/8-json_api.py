#!/usr/bin/python3
"""
This Python script takes a letter as input and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter. The
letter is sent in the variable q. If no argument is given, q is set to
an empty string.
"""
import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) < 2:
        q = ""
    else:
        q = argv[1]

    url = "http://0.0.0.0:5000/search_user"
    data = {"q": q}

    response = requests.post(url, data=data)

    try:
        json_response = response.json()
        if len(json_response) > 0:
            user_data = json_response
            print("[{}] {}".format(user_data["id"], user_data["name"]))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
