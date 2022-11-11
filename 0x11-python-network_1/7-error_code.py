#!/usr/bin/python3
""" A script that takes in a URL and sends a request to
    the URL and displays the body of the response while
    handling exceptions
"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    r = requests.get(url)

    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)
