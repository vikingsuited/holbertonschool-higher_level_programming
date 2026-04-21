#!/usr/bin/python3
"""
Sends a request to a URL and displays the body of the response.
If the status code is >= 400, prints the error code.
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    r = requests.get(url)
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)
