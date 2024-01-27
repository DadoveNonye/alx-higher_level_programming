#!/bin/bash

# Take URL as a command-line argument and send a GET request to display the body
curl -s -L "$1"
