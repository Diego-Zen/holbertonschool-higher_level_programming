#!/usr/bin/python3
"""
    Response header value module
"""
import sys
from urllib import request

if __name__ == "__main__":
    with request.urlopen(sys.argv[1]) as response:
        resp = response.info().get("x-request-id")
        print(resp)
