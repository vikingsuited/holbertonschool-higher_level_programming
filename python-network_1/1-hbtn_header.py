#!/usr/bin/python3
"""
Sends a request to a URL and displays the value of the X-Request-Id variable
found in the header of the response.
"""
import urllib.request
import sys


if __name__ == "__main__":
    if len(sys.argv) > 1:
        url = sys.argv[1]
        with urllib.request.urlopen(url) as response:
            print(response.getheader('X-Request-Id'))
