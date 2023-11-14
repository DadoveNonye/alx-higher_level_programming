#!/usr/bin/python3
"""Defining a base class"""
import json
import csv
import turtle
class Base:
    """implementing the base model"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initialization of the base class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
    @staticmethod
    def to_json_string(list_dictionaries):
        """static method that returns the JSON
            string representation of list_dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """static method  that returns the list of the
            JSON string representation json_string
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """class method that writes the JSON string
            representation of list_objs to a file
        """
        if list_objs is None:
            list_objs = []

        filename = cls.__name__ + ".json"
        json_string = cls.to_json_string([obj.to_dictionary() for obj in list_objs])

        with open(filename, 'w') as f:
            f.write(json_string)

    @classmethod
    def load_from_file(cls):
        """class method  that returns a list of instances"""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, 'r') as file:
                json_string = file.read()
                dictionaries = cls.from_json_string(json_string)
                return [cls.create(**dict) for dict in dictionaries]
        except FileNotFoundError:
            return []

    @classmethod
    def create(cls, **dictionary):
        """a class method that returns an instance
            with all attributes already set
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)  
            """Create a dummy Rectangle instance"""
        elif cls.__name__ == "Square":
            dummy = cls(1)  
            """Create a dummy Square instance"""
        else:
            dummy = cls()  
            """For other classes, create a dummy instance"""

        dummy.update(**dictionary)  
        """Update the dummy instance with real values"""
        return dummy

    def update(self, *args, **kwargs):
        if args:
            attrs = ["id", "width", "height", "size"]
            for attr, value in zip(attrs, args):
                setattr(self, attr, value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draws Rectangles and Squares using the turtle module.

        Args:
            list_rectangles: A list of Rectangle objects to draw.
            list_squares: A list of Square objects to draw.
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#ffffff")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#b5e3d8")
        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for i in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()
