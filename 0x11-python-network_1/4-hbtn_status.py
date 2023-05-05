#!/usr/bin/python3
"""
This Python script fetches https://alx-intranet.hbtn.io/status and
displays the body of the response in a specific format using requests
"""
import requests


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    response = requests.get(url)

    print("Body response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))
