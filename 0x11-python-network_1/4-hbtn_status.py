#!/usr/bin/python3
"""
    fetches url
"""
from urllib import request

if __name__ == "__main__":
    with request.urlopen("https://intranet.hbtn.io/status") as response:
        resp = response.read()
        cont = resp.decode('utf-8')
        print("Body response:")
        print(
            "\t- type: {}\n\t- content: {}"
            .format(type(cont), cont)
        )
