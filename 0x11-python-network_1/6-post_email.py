#!/usr/bin/python3
""" A script that takes in a URL and sends a POST request to
    the URL with an email as a parameter and displays the body
    of the response
"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}
    r = requests.post(url, data=value)
    print(r.text)
