#!/usr/bin/python3
"""
Sends a request to the URL and displays the body of the response
(decoded in utf-8)
if the http status code is equal to or greater than 400
Error code: followed by the HTTP status code
else print response

Usage:
    <module_name.py> <url>

Return:
    content OR
    error code
"""

import sys
import requests


def main():
    url = sys.argv[1]

    r = requests.get(url)

    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))

    else:
        print(r.text)


if __name__ == "__main__":
    main()
