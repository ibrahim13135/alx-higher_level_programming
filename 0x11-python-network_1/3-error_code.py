#!/usr/bin/python3
"""Sends a request to a given URL and displays the body of the response.

Usage: ./3-error_code.py <URL>
    - Displays the body of the response.
    - Manages urllib.error.HTTPError exceptions and prints the error code.
"""

import sys

import urllib.request
import urllib.error

if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
