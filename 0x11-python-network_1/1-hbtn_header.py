#!/usr/bin/python3
""" A script that takes in a URL, sends a request to the URL and
displays the value of the "X-Request-Id" found in the header of the response
"""
import urllib.request
import sys

if __name__ == "__main__":
    req = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(req) as response:
        html = response.info()
        print(html.get("X-Request-Id"))
