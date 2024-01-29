#!/usr/bin/python3
import requests
import sys
# A Python script that takes in a URL, sends a request to the URL
def get_x_request_id(url):
    try:
        response = requests.get(url)
        x_request_id = response.headers.get('X-Request-Id')

        if x_request_id:
            print(f"{x_request_id}")
        else:
            print("X-Request-Id not found in the response headers.")
    except requests.exceptions.RequestException as e:
        print(f"Error accessing the URL: {e}")

if __name__ == "__main__":
    url = sys.argv[1]
    get_x_request_id(url)
