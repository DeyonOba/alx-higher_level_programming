#!/usr/bin/python3
"""
Sends a request to the URL and displays the body of the response
(decoded in utf-8)
manage urllib.error.HTTPError exceptions and print:
Error code: followed by the HTTP status code

Usage:
    <module_name.py> <url>

Return:
    content OR
    error code
"""

import sys
import urllib.request
import urllib.error


def main():
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            body = response.read()
            utf8_content = body.decode("utf-8")
            print(utf8_content)
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code()))


if __name__ == "__main__":
    main()
