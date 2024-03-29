#!/usr/bin/python3
"""
Module takes in a letter and sends a post request to
http://0.0.0.0:5000/search_user with the letter as parameter

The letter is stored in the parameter q,
if no arguement is give value is an empty string
if the response body is a proper JSON return [<id>] name
Display Not a valid JSON if the JSON is invalid
Display No result if the JSON is empty
"""
import sys
import requests


def main():
    url = "http://0.0.0.0:5000/search_user"

    if len(sys.argv) == 1:
        letter = ""
    else:
        letter = sys.argv[1]

    payload = {"q": letter}
    try:
        response = requests.post(url, data=payload)

        data = response.json()
        if data:
            print("[{}] {}".format(data["id"], data["name"]))
        else:
            print("No result")
    except:
        print("Not a valid JSON")


if __name__ == "__main__":
    main()
