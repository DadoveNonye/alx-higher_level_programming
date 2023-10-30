#!/usr/bin/python3
"""Prints square with the character #"""
def print_square(size):
    """Prints a square
    Args:
        size = length of square
    Raises:
        TypeError if size is not an integer
        ValueError if size is less than 0
    """
    character = "#"
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if (size < 0):
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and (size < 0):
        raise TypeError("size must be an integer")
    print((("#" * size + "\n") * size), end="")
