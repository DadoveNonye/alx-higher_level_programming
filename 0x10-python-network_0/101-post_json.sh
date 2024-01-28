#!/bin/bash
# A Bash script that sends a JSON POST request to a URL passed as the first arg
curl -sX POST "$1" -H "Content-Type: application/json" --data-binary @"$2"
