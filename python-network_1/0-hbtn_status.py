#!/usr/bin/python3
import urllib.request

url = "http://0.0.0.0:5050/status"

try:
    with urllib.request.urlopen(url) as response:
        content = response.read()

    print("Body response:")
    print("\t- type: {}".format(type(content)))
    print("\t- content: {}".format(content))
    print("\t- utf8 content: {}".format(content.decode('utf-8')))
except urllib.error.URLError as e:
    print("[stderr]:", e.reason)
