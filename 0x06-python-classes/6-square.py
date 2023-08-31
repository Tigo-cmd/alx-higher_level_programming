#!/usr/bin/python3
"""This module defines a class"""


class Square:
    """An empty class that defines a square
    __init__: initializes the constructor
    """

    def __init__(self, size=0, position=(0, 0)):
        """Defines an attribute and initializes the size attribute
        size: size of the square many things depend on it (area computation, etc.)
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Getter function for size this sets the size variable"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter function for Size which initializes the size to value"""
        if not isinstance(value, int):
            raise TypeError("Size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Public attribute that returns the current square area"""
        return self.__size ** 2

    @property
    def position(self):
        """position getter function for the square class returns the position"""
        return self.__position

    @position.setter
    def position(self, value):
    """Position setter function which sets the position to the value passsed in
       and checks if the value is an integer or < 0 otherwise it rasies 
       an execption
    """
        self.__position = value
        for i in value:
            if not isinstance(i, int) or i < 0:
                raise ValueError("position must be a tuple of 2 positive integers")

    def my_print(self):
        """this function prints in stdout the square with the character #"""
        if self.__size == 0:
            print()
        else:
            if self.__position[1] > 0:
                print()
            for i in range(0, self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)
