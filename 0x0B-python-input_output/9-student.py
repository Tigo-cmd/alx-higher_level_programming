#!/usr/bin/python3
"""Defines a student class module"""
import json


class Student:
    """a class Student that defines a student initials"""
    def __init__(self, first_name, last_name, age):
        """initializing function at first callS
           first_name: students first name
           last_name: students last name
           age: students age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        
    def to_json(self):
        """retrieves a dictionary representation of a Student instance"""
        return self.__dict__
