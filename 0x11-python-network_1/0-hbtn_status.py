#!/usr/bin/python3
import urllib.request
# A Python script that fetches a URL
url = 'https://alx-intranet.hbtn.io/status'

with urllib.request.urlopen(url) as response:
    content = response.read()
    print("Body response:")
    print("\t- type:", type(content))
    print("\t- content:", content.decode('utf-8'))
