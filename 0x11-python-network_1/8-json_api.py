#!/usr/bin/python3
import requests
import sys

def search_user(letter):
    try:
        url = 'http://0.0.0.0:5000/search_user'
        payload = {'q': letter}

        response = requests.post(url, data=payload)
        json_data = response.json()

        if json_data:
            print(f"[{json_data['id']}] {json_data['name']}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
    except requests.exceptions.RequestException as e:
        print(f"Error sending POST request: {e}")

if __name__ == "__main__":
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    search_user(letter)
