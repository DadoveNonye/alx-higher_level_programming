#!/usr/bin/python3

"""Defines a class object"""

class BaseGeometry():
    """Public instance method"""
    def area(self):
        """raises an exception"""
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """public instance that validates value
            Args: self, name, value
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    """Defines a rectangle class"""
    def __init__(self, width, height):
        """initializes a new rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
