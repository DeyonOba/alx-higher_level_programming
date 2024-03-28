#!/usr/bin/python3
"""
Script that fetches https://alx-intranet.hbtn.io/status
"""
import requests


def main():
    url = "https://alx-intranet.hbtn.io/status"

    r = requests.get(url)
    print("Body response:")
    print("\t- type:", type(r.text))
    print("\t- content:", r.text)


if __name__ == "__main__":
    main()
