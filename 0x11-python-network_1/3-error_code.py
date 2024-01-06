#!/usr/bin/python3
""" Script that takes in a URL, sends a request to the URL and displays
    the body of the response (decoded in utf-8).
"""

import urllib.request
import urllib.error
import sys


if __name__ == "__main__":
    Url = sys.argv[1]

    try:
        with urllib.request.urlopen(Url) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
