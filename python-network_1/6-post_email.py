#!/usr/bin/python3
"""Documented now"""
import requests
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    value = sys.argv[2]
    response = requests.post(url, data={"email": value})
    print("{}".format(response.text))
