#!/usr/bin/python3
""" Script that takes in a URL, sends a request to the URL and displays
    the body of the response.
"""

import requests
import sys

if __name__ == "__main__":
    Url = sys.argv[1]

    response = requests.get(Url)
    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)
