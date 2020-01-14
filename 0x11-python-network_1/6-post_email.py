#!/usr/bin/python3
"""
    Post an email module
"""
import sys
import requests

if __name__ == "__main__":
    r = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    print(r.text)
