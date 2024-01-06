#!/usr/bin/python3
""" Script that takes your GitHub credentials (username and password)
    and uses the GitHub API to display your id
"""

import requests
import sys

if __name__ == "__main__":
    Username = sys.argv[1]
    Password = sys.argv[2]

    response = requests.get('https://api.github.com/user',
                            auth=(Username, Password))
    print(response.json().get('id'))
