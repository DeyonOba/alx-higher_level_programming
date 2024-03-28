#!/usr/bin/python3
"""
Module takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
"""

import sys
import urllib.request
import urllib.parse


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    data_dict = {"email": email}
    data = urllib.parse.urlencode(data_dict)
    data = data.encode("utf-8")
    req = urllib.request.Request(url, data, method="POST")

    with urllib.request.urlopen(req) as response:
        response_data = response.read().decode("utf-8")
        print(response_data)
