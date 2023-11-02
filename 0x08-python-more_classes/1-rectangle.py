#!/usr/bin/python3
""" Defines a rectangle """
class Rectangle:
    """Represents a rectangle class"""
    def __init__(self, width=0, height=0):
        """initilize a rectangle class

        Args:
        width: represents the width
        height: represents the height"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """property to retrive width"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            """setter to see width"""
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
        """setter to see height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("eight must be >= 0")
        self.__height = value
