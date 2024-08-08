#!/usr/bin/python3
"""
Documentation
Fetches data from the url using
the urllib module in python
"""

import urllib.request

url = 'https://intranet.hbtn.io/status'
if url.startswith('https://'):
    url = 'https://alu-intranet.hbtn.io/status'

if __name__ == '__main__':
    with urllib.request.urlopen(url) as f:
        content = f.read()
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content.decode('utf-8')))
