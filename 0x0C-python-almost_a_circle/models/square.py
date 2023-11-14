#!/usr/bin/python3
"""Defines a square method"""
from models.rectangle import Rectangle

class Square(Rectangle):
    """Class Square inherits from Rectangle."""
    def __init__(self, size, x=0, y=0, id=None):
        """Initializes a new Square."""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for size."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size."""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Public method that assigns attributes to the Square."""
        if args:
            attr_list = ['id', 'size', 'x', 'y']
            for i, arg in enumerate(args):
                setattr(self, attr_list[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Public method that returns the dictionary
            representation of a Square.
        """
        return {'id': self.id, 'size': self.width, 'x': self.x, 'y': self.y}

    def __str__(self):
        """Returns the string representation of the Square."""
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.width)
