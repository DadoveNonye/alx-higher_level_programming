#!/usr/bin/python3
"""An i/o function that appends a file"""
def append_write(filename="", text=""):
    """Appends a sting to a text file
        Args:
            filename:name of the file
            text: the str to append
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
