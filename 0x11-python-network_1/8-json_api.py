#!/usr/bin/python3
""" A Python script that takes in a letter sends a POST request to
    http://0.0.0.0:5000/search_user with the letter q as a parameter
"""
import sys
import requests

if __name__ == "__main__":
    letter = "" if len(sys.argv) == 1 else sys.argv[1]
    payload = {"q": letter}

    res = requests.post("http://0.0.0.0:5000/search_user", data=payload)
    try:
        res_json = res.json()
        if res_json == {}:
            print("No result")
        else:
            print("[{}] {}".format(res_json.get("id"), res_json.get("name")))
    except ValueError:
        print("Not a valid JSON")
