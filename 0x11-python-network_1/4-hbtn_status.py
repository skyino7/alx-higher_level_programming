#!/usr/bin/python3

""" Script that fetches https://intranet.hbtn.io/status """


import requests

if __name__ == "__main__":
    Url = "https://intranet.hbtn.io/status"

    response = requests.get(Url)
    html = response.text

    print("Body response:")
    print("\t- type: {}".format(type(html)))
    print("\t- content: {}".format(html))
    print("\t- utf8 content: {}".format(html))
