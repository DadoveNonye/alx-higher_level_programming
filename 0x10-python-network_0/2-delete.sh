#!/bin/bash
# A Bash script that sends a DELETE request to the URL passed as the first arg
curl -s -X DELETE "$1"
