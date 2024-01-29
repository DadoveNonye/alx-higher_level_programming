#!/usr/bin/python3
import requests
import sys

def get_url_content(url):
    try:
        response = requests.get(url)
        print("Response Body:")
        print(response.text)

        # Check if HTTP status code is greater than or equal to 400
        if response.status_code >= 400:
            print(f"Error code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error accessing the URL: {e}")

if __name__ == "__main__":
    url = sys.argv[1]
    get_url_content(url)
