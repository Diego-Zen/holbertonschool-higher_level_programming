#!/usr/bin/python3
"""
    Takes github credentials and uses the Github API module
"""
import sys
import requests

if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[1], sys.argv[2]
    )
    r = requests.get(url)
    try:
        json_data = r.json()
        for data in json_data:
            print("{}: {}".format(
                data.get('sha'),
                data['commit']['author'].get('name'))
            )
    except ValueError:
        print("Not a valid JSON")
