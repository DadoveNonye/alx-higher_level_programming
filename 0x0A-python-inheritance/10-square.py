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

    def area(self):
        """Area method"""
        return self.__width * self.__height
    def __str__(self):
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))

class Square(Rectangle):
    """Represents a square"""
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
