#!/usr/bin/python3
"""
Sends a POST request to http://0.0.0.0:5000/search_user
with a letter as a parameter.
"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) < 2:
        q = ""
    else:
        q = sys.argv[1]

    payload = {'q': q}
    url = "http://0.0.0.0:5000/search_user"

    try:
        r = requests.post(url, data=payload)
        # JSON cavabını lüğətə çeviririk
        response_json = r.json()

        if response_json == {}:
            print("No result")
        else:
            id_val = response_json.get('id')
            name_val = response_json.get('name')
            print("[{}] {}".format(id_val, name_val))
    except ValueError:
        print("Not a valid JSON")
