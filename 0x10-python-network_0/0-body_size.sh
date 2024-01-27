#!/bin/bash
# Send a HEAD request to the URL and extract Content-Length from the response headers
size=$(curl -sI "$url" | grep -i Content-Length | awk '{print $2}')
