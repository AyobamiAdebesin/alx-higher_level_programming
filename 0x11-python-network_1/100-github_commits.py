#!/usr/bin/python3
""" A script that shows the last 10 commits of a user"""
import requests
import sys

if __name__ == "__main__":
    repo_name = sys.argv[1]
    user_name = sys.argv[2]

    res = requests.get("https://api.github.com/repos/{}/{}/commits\
            ".format(user_name, repo_name))
    commits = res.json()
    try:
        for i in range(10):
            print("{}: {}".format(
                commits[i].get("sha"),
                commits[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
