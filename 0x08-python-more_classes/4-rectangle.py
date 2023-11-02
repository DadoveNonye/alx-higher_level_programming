#!/usr/bin/python3
#4-rectangle.py
"""Defines a rectangle"""

class Rectangle:
    """Represents a rectangle"""
    def __init__(self, width=0, height=0):
        """Initializes a rectangle
        Args:
        width: width of he rectangle
        height: height of the rectangle
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """property to retirve width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for the width of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """property to retrieve height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for the height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """set the area"""
        return self.width * self.height

    def perimeter(self):
        """setter for the perimeter"""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Returns a printable rep of the rect
        with the character # as str
        """
        if self.width == 0 or self.height == 0:
            return ""

        rectangle_str = ""
        for _ in range(self.height):
            rectangle_str += "#" * self.width + "\n"
        return rectangle_str[:-1]

    def __repr__(self):
        """recreating a new instance using eval"""
        return f"Rectangle({self.width}, {self.height})"
