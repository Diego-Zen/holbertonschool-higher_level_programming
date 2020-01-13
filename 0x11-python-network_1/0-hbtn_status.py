#!/usr/bin/python3
"""
    fetches url
"""
from urllib import request

if __name__ == "__main__":
    with request.urlopen("https://intranet.hbtn.io/status") as response:
        resp = response.read()
        charset = resp.decode('utf-8')
        print("Body response:")
        print(
            "\t- type: {}\n\t- content: {}\n\t- utf8 content: {}"
            .format(type(resp), resp, charset)
        )
