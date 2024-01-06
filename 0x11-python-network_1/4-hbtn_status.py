#!/usr/bin/python3

""" Script that fetches https://intranet.hbtn.io/status """


import requests

if __name__ == "__main__":
    Url = "https://intranet.hbtn.io/status"

    response = requests.get(Url)
    html = response.text

    getType = type(html)
    print(f"Body response:\n\t- type: {getType}\n\t- content: {html}")
