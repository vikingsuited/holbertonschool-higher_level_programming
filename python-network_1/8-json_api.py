#!/usr/bin/python3
"""
Sends a POST request to http://0.0.0.0:5000/search_user with a letter as a parameter.
The letter is sent in the variable 'q'.
"""
import requests
import sys


if __name__ == "__main__":
    # Əgər arqument verilməyibsə q = "", əks halda birinci arqument
    if len(sys.argv) < 2:
        q = ""
    else:
        q = sys.argv[1]

    payload = {'q': q}
    url = "http://0.0.0.0:5000/search_user"

    try:
        r = requests.post(url, data=payload)
        # JSON cavabını lüğətə (dict) çevirməyə çalışırıq
        response_json = r.json()

        if response_json == {}:
            print("No result")
        else:
            print("[{}] {}".format(response_json.get('id'), response_json.get('name')))
    except ValueError:
        # Əgər r.json() xəta verirsə (məsələn, cavab JSON deyil), bu blok işləyir
        print("Not a valid JSON")
