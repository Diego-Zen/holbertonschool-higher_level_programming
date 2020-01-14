#!/usr/bin/python3
"""
    Takes in a url, sends a request to the url and displays the body module
"""
import sys
from urllib import request
from urllib import parse
from urllib import error

if __name__ == "__main__":
    try:
        with request.urlopen(url=sys.argv[1]) as response:
            data = response.read()
            dec = data.decode('utf-8')
            print(dec)
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
