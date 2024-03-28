#!/usr/bin/python3
"""
Script that fetches https://alx-intranet.hbtn.io/status
"""
import requests


def main():
    url = "https://alx-intranet.hbtn.io/status"

    r = requests.get(url)
    print("Body response:")
    print("\t- type:", type(r.content.decode("utf-8")))
    print("\t- content:", r.content.decode("utf-8"))


if __name__ == "__main__":
    main()
