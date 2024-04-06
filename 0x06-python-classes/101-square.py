#!/usr/bin/python3
"""Square class module"""


class Square:
    """ an empty class Square that defines a square"""
    def __init__(self, size=0, position=(0, 0)):
        """ constructor for Square method
            Args:
                size (int) : private instance attribute
                position (tuple (int, int)): position of the square position
        """
        self.__size = size
        self.__position = position

    @property
    def position(self):
        """get/set property for position"""
        return self.__position

    @position.setter
    def position(self, value):
        """set property for position"""
        if len(value) != 2 or not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    @property
    def size(self):
        """getter property for size attribute"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """returns the current square area
           Args:
               size: private instance attribute
        """
        return self.__size ** 2

    def my_print(self):
        """prints in stdout the square with the character #"""
        if self.__size == 0:
            print()
        else:
            [print("") for i in range(0, self.__position[1])]
            for i in range(0, self.__size):
                [print(" ", end="") for j in range(0, self.__position[0])]
                [print("#", end="") for k in range(0, self.__size)]
                print("")
    
    def __str__(self):
        """replicate the print rep for square"""
        if self.__size != 0:
            [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            if i != self.__size - 1:
                print("")
        return ""
