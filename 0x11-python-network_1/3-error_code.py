import urllib.request
import urllib.error
import sys

# A Python script that takes in a URL,
# sends a request to the URL and displays the body of the response
def get_url_content(url):
    try:
        with urllib.request.urlopen(url) as response:
            # Read and decode the response body
            response_body = response.read().decode('utf-8')
            print("Response Body:")
            print(response_body)
    except urllib.error.HTTPError as e:
        # Handle HTTP errors
        print(f"Error code: {e.code}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <URL>")
    else:
        url = sys.argv[1]
        get_url_content(url)
