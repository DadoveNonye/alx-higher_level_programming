import urllib.request
import urllib.parse
import sys

# Python script that takes in a URL and an email,
# sends a POST request to the passed URL with the email as a parameter

def send_post_request(url, email):
    try:
        # Prepare data to be sent in the POST request
        data = urllib.parse.urlencode({'email': email}).encode('utf-8')

        with urllib.request.urlopen(url, data) as response:
            response_body = response.read().decode('utf-8')

            print("Response Body:")
            print(response_body)
    except urllib.error.URLError as e:
        print(f"Error accessing the URL: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <URL> <email>")
    else:
        url = sys.argv[1]
        email = sys.argv[2]
        send_post_request(url, email)
