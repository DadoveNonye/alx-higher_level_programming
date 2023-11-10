#!/usr/bin/python3
"""An i/o function that reads a text file"""
def read_file(filename=""):
    """prints to stdout
        Args:
            filename: name of the file
    """
    with open(filename, encoding="utf-8") as f:
        for line in f:
            print(line, end="")
