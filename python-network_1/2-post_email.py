#!/usr/bin/python3
"""
Sends a POST request to a URL with an email as a parameter
and displays the body of the response.
"""
import urllib.parse
import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    values = {'email': email}
    
    # Məlumatı URL-kodlaşdırılmış formata salırıq
    data = urllib.parse.urlencode(values)
    # Məlumatı baytlara (bytes) çeviririk
    data = data.encode('ascii')
    
    # POST sorğusu yaratmaq üçün data parametrini urlopen-a ötürürük
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
