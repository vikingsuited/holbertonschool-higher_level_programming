#!/usr/bin/python3
"""
Uses the GitHub API to display the user id using Basic Authentication.
The script takes GitHub username and Personal Access Token as arguments.
"""
import requests
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    url = "https://api.github.com/user"
    r = requests.get(url, auth=(username, password))

    try:
        user_data = r.json()
        print(user_data.get('id'))
    except ValueError:
        print("None")
