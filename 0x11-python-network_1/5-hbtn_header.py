#!/usr/bin/python3
"""
Script that fetches https://alx-intranet.hbtn.io/status
"""
import sys
import requests


def main():
    url = sys.argv[1]

    r = requests.get(url)
    print(r.headers.get("X-Request-Id"))


if __name__ == "__main__":
    main()
