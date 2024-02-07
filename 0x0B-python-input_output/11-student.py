#!/usr/bin/python3
"""
Student to disk and reload module
"""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        """Initialize a student with first_name, last_name, and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return the dictionary representation of a Student instance"""
        if attrs is None:
            return self.__dict__
        return {key: self.__dict__[key]
                for key in attrs if key in self.__dict__}

    def reload_from_json(self, json):
        """Replace all attributes of the Student
            instance with the given dictionary"""
        self.__dict__.update(json)
