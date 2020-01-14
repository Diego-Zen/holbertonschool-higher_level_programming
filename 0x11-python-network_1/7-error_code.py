#!/usr/bin/python3
"""
    Error code module
"""
import sys
import requests

if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    status = r.status_code
    if (status >= 400):
        print("Error code: {}".format(status))
    else:
        print(r.text)
