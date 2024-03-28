#!/usr/bin/python3
"""Module fetches info from url: https://alx-intranet.hbtn.io/status"""

import urllib.request

def main():
    url = "https://alx-intranet.hbtn.io/status"
    with urllib.request.urlopen(url) as response:
        body = response.read()
        utf8_content = body.decode("utf-8")

    print("Body response:")
    print(f"    - type: {type(body)}")
    print(f"    - content: {body}")
    print(f"    - utf8 content: {utf8_content}")

if __name__ == "__main__":
    main()
