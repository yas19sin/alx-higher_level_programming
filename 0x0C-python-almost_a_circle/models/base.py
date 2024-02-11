#!/usr/bin/python3
"""Base module"""
import json
import csv
import turtle
from random import randrange


class Base:
    """Base class for all other classes in the project."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new instance of the Base class."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Convert a list of dictionaries to a JSON string."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Convert a JSON string to a list of dictionaries."""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save a list of objects to a file in JSON format."""
        filename = cls.__name__ + ".json"
        obj_list = []
        if list_objs is not None:
            for obj in list_objs:
                obj_list.append(obj.to_dictionary())
        with open(filename, "w") as file:
            file.write(cls.to_json_string(obj_list))

    @classmethod
    def load_from_file(cls):
        """Load a list of objects from a file in JSON format."""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as file:
                json_string = file.read()
                dict_list = cls.from_json_string(json_string)
                obj_list = [cls.create(**obj_dict) for obj_dict in dict_list]
                return obj_list
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Save a list of objects to a file in CSV format."""
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            if cls.__name__ == "Rectangle":
                headers = ["id", "width", "height", "x", "y"]
            elif cls.__name__ == "Square":
                headers = ["id", "size", "x", "y"]
            writer.writerow(headers)
            if list_objs is not None:
                for obj in list_objs:
                    writer.writerow([getattr(obj, key) for key in headers])

    @classmethod
    def load_from_file_csv(cls):
        """Load a list of objects from a file in CSV format."""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r") as file:
                reader = csv.reader(file)
                obj_list = []
                for row in reader:
                    if cls.__name__ == "Rectangle":
                        if row[0] == "id":
                            continue
                        print(f"{row[0]}")
                        obj_dict = {
                            "id": int(row[0]),
                            "width": int(row[1]),
                            "height": int(row[2]),
                            "x": int(row[3]),
                            "y": int(row[4]),
                        }
                    elif cls.__name__ == "Square":
                        if row[0] == "id":
                            continue
                        obj_dict = {
                            "id": int(row[0]),
                            "size": int(row[1]),
                            "x": int(row[2]),
                            "y": int(row[3]),
                        }
                    obj_list.append(cls.create(**obj_dict))
                return obj_list
        except FileNotFoundError:
            return []
    
    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        instance = cls(1, 1)
        instance.x = 0
        instance.y = 0
        instance.update(**dictionary)
        return instance

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Opens a Turtle window and draws
        rectangles and squares.

        Args:
            - list_rectangles: list of Rectangle instances
            - list_squares: list of Square instances
        """

        turtle.speed(2)
        turtle.bgcolor("white")

        for i in (list_rectangles + list_squares):
            t = turtle.Turtle()
            t.color("black")
            t.pensize(3)
            t.penup()
            t.setpos(0, 0)
            turtle.Screen().colormode(255)
            t.pencolor((randrange(255), randrange(255), randrange(255)))
            Base.draw_shape(t, i)
            turtle.hideturtle()

        turtle.exitonclick()

    @staticmethod
    def draw_shape(t, shape):
        """Helper method to draw a Rectangle or Square."""
        t.penup()
        t.setpos(shape.x, shape.y)
        t.pendown()
        for _ in range(4):
            t.forward(shape.width)
            t.left(90)
