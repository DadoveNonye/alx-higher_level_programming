#!/usr/bin/python3
"""define a square"""
class Square:
    """Define a square."""

    def __init__(self, size=0):
        """Initializes a new square.

        Args:
            size (int): Size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Returns the current square's area."""
        return self.__size ** 2
