#!/usr/bin/python3
"""class Student that defines a student by:"""


class Student:
    """
     class Student that defines a student by:

    Public instance attributes:
        first_name
        last_name
        age
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        retrieves a dictionary representation
         of a Student instance (same as 8-class_to_json.py)
        """
        if isinstance(attrs, list):
            for i in attrs:
                if all(type(i)) is str:
                    for j in attrs:
                        if hasattr(self, j):
                            return {getattr(self, j)}
                        else:
                            return {j}
        return self.__dict__
