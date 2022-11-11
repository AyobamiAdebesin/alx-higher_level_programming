#!/usr/bin/python3
"""A Python script that fetches a url and returns a response"""
import urllib.request


if __name__ == "__main__":
    req = urllib.request.Request('http://alx-intranet.hbtn.io/status')
    with urllib.request.urlopen(req) as response:
        the_page = response.read()
        print('Body response:')
        print("\t- type: {}".format(type(the_page)))
        print("\t- content: {}".format(the_page))
        print("\t- utf8 content: {}".format(the_page.decode("utf-8")))
