#!/usr/bin/python3
"""call content"""

import urllib.request
import urllib.error
import sys

if __name__ == '__main__':
    """"Message"""
    url = sys.argv[1]
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as response:
            data = response.read()
            print("{}".format(data.decode("utf-8")))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
    except urllib.error.URLError as e:
        print(e.reason)
