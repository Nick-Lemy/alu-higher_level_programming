#!/usr/bin/python3
"""Documented now"""
import requests
import requests.auth
import sys

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    response = requests.get(
        url="https://api.github.com/user",
        auth=(requests.auth.HTTPBasicAuth(
            username,
            password
        )))
    try:
        json_response = response.json()
        print("{}".format(json_response["id"]))
    except:
        print(None)
