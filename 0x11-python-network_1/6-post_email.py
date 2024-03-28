#!/usr/bin/python3
"""
Script sends a POST request to the passed URL with the email as a parameter,
and finally displays the body of the response.
"""
import sys
import requests


def main():
    url = sys.argv[1]
    email = sys.argv[2]

    param = {"email": email}
    r = requests.post(url, data=param)

    print(r.content.decode())


if __name__ == "__main__":
    main()
