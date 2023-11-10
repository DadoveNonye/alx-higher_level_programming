#!/usr/bin/python3
"""Defines an input and output fintions"""
def write_file(filename="", text=""):
    """writes a file and return the count of the file"""
    with open(filename, mode="w", encoding="utf-8") as f:
        count = f.write(text)
    return count
