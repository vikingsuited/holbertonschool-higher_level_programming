#!/usr/bin/python3
"""
Sends a request to a URL and displays the body of the response.
Manages urllib.error.HTTPError exceptions to print the error code.
"""
import urllib.error
import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
