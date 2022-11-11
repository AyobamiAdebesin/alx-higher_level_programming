#!/usr/bin/python3
""" A Python Script that fetches URL with the request library"""
import requests

if __name__ == "__main__":
    req = requests.get("https://intranet.hbtn.io/status")
    t = req.text
    print("Body response:\n\t- type: {}\n\t- content: {}".format(type(t), t))
