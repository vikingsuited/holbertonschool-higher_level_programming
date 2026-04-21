#!/usr/bin/python3
"""
Sends a request to a URL and displays the value of the
X-Request-Id variable found in the response header.
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    r = requests.get(url)
    # requests.get(url).headers bir lüğətdir (dict-like object)
    print(r.headers.get('X-Request-Id'))
