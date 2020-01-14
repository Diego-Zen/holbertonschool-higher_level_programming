#!/usr/bin/python3
"""
    Star Wars api search module
"""
import sys
import requests

if __name__ == "__main__":
    search = sys.argv[1]
    r = requests.get('https://swapi.co/api/people/', params={'search': search})
    try:
        json_data = r.json()
        print("Number of results: {}".format(json_data.get('count')))
        for test in json_data['results']:
            print(test.get('name'))
    except ValueError:
        print("Not a valid JSON")
