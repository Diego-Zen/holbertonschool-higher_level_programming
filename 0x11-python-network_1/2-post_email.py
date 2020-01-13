#!/usr/bin/python3
"""
    Takes a url and a an email and sends a post request module
"""
import sys
from urllib import request
from urllib import parse

if __name__ == "__main__":
    post_data = parse.urlencode({'email': sys.argv[2]}).encode('ascii')
    with request.urlopen(url=sys.argv[1], data=post_data) as post_response:
        data = post_response.read()
        dec = data.decode('ascii')
        print(dec)
