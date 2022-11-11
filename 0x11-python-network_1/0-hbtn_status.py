#!/usr/bin/python3
"""A Python script that fetches a url and returns a response"""
import urllib.request

if __name__ == "__main__":
    with urllb.request.urlpen("https://intranet.hbtn.io/status") as response:
        html = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format(html))
        print("\t- utf8 content: {}".format(html.decode("utf-8")))
