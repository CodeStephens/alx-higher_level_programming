#!/usr/bin/python3
import urllib.request
"""
This Python script fetches `https://alx-intranet.hbtn.io/status`
"""
url = "https://alx-intranet.hbtn.io/status"


if __name__ = '__main__':
    with urllib.request.urlopen(url) as response:
        html = response.read()

    print("\t- type: {}".format(type(html)))
    print("\t- content: {}".format(html))
    print("\t- utf8 content: {}".format(html.decode('utf-8')))