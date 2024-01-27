#!/bin/bash
# A Bash script that takes in a URL and displays all HTTP methods
curl -sI -X OPTIONS "$1" | awk '/Allow/ {print $2}'
