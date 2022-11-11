#!/usr/bin/python3
""" A Python script that sends a request to a URL and extract
    information in the header of the response
"""
import requests
import sys

if __name__ == "__main__":
    res = requests.get(sys.argv[1])
    print(res.headers.get("X-Request-Id"))
