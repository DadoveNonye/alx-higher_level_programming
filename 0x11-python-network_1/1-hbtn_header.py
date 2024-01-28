#!/usr/bin/python3
import urllib.request
import sys
# Python script that takes in a URL,
# sends a request to the URL and displays the value of the X-Request-Id var
def get_x_request_id(url):
    try:
        with urllib.request.urlopen(url) as response:
            x_request_id = response.headers.get('X-Request-Id')
            if x_request_id:
                print(f"X-Request-Id: {x_request_id}")
            else:
                print("X-Request-Id not found in the response headers.")
    except urllib.error.URLError as e:
        print(f"Error accessing the URL: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <URL>")
    else:
        url = sys.argv[1]
        get_x_request_id(url)
