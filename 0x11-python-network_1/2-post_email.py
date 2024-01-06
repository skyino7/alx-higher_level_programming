#!/usr/bin/python3

""" Script that takes in a URL and an email address, sends a POST request
    to the passed URL with the email as a parameter, and displays the body
    of the response (decoded in utf-8)
"""

import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    Url = sys.argv[1]
    Email = sys.argv[2]

    data = urllib.parse.urlencode({'email': Email})
    data = data.encode('ascii')

    with urllib.request.urlopen(Url, data) as response:
        print(response.read().decode('utf-8'))
