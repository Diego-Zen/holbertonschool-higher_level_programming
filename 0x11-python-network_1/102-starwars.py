#!/usr/bin/python3
"""
    Star Wars api search movies by character module
"""
import sys
import requests

if __name__ == "__main__":

    url = 'https://swapi.co/api/people/'
    payload = {'search': sys.argv[1]}
    page = 2

    r = requests.get(url, params=payload)
    try:
        json_data = r.json()
        print("Number of results: {}".format(json_data.get('count')))

        for test in json_data['results']:
            print(test.get('name'))
            for i in test.get('films'):
                resp = requests.get(i)
                data = resp.json()
                print("\t{}".format(data.get('title')))

        while json_data.get('next') is not None:
            payload2 = {'search': sys.argv[1], 'page': page}
            response = requests.get(url, params=payload2)
            json_data = response.json()

            for result in json_data['results']:
                print(result.get('name'))
                for i in result.get('films'):
                    resp = requests.get(i)
                    data = resp.json()
                    print("\t{}".format(data.get('title')))

            page = page + 1
    except ValueError:
        print("Not a valid JSON")
