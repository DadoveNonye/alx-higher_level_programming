#!/usr/bin/python3
class Rectangle:
    """Represents a rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes a rectangle
        Args:
        width: width of the rectangle
        height: height of the rectangle
        """
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Property to retrieve width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for the width of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Property to retrieve height"""
        return self.__height 

    @height.setter
    def height(self, value):
        """Setter for the height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates the area"""
        return self.width * self.height

    def perimeter(self):
        """Calculates the perimeter"""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Returns a printable representation of the rectangle with '#' as the character"""
        if self.width == 0 or self.height == 0:
            return ""

        rectangle_str = ""
        for _ in range(self.height):
            rectangle_str += str(self.print_symbol) * self.width + "\n"
        return rectangle_str[:-1]

    def __repr__(self):
        """Returns a string that can recreate a new instance using eval"""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """Deletes a rectangle"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compares two rectangles based on area and returns the bigger one"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        area_1 = rect_1.width * rect_1.height
        area_2 = rect_2.width * rect_2.height

        if area_1 >= area_2:
            return rect_1
        else:
            return rect_2
