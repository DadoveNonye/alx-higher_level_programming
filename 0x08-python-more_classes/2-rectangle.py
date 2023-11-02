#!/usr/bin/python3
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
            raise ValueError("eight must be >= 0")
        self.__height = value

    def area(self):
        """set the area"""
        return self.width * self.height

    def perimeter(self):
        """setter for the perimeter"""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)
