#!/usr/bin/python3
import requests
import sys
# Python script that takes in a URL and an email address, sends a POST
def send_post_request(url, email):
    try:
        payload = {'email': email}
        response = requests.post(url, data=payload)
        print("Response Body:")
        print(response.text)
        print(f"Your email is: {email}")
    except requests.exceptions.RequestException as e:
        print(f"Error sending POST request: {e}")

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    send_post_request(url, email)
