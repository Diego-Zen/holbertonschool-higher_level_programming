#!/usr/bin/python3
"""
    Search api, takes in a letter and sends a post request module
"""
import sys
import requests

if __name__ == "__main__":
    search = ""

    if len(sys.argv) > 1:
        search = sys.argv[1]
    r = requests.post('http://0.0.0.0:5000/search_user', data={'q': search})
    try:
        json_data = r.json()
        if len(json_data) == 0:
            print("No result")
        else:
            print("[{}] {}".format(json_data.get('id'), json_data.get('name')))
    except ValueError:
        print("Not a valid JSON")
