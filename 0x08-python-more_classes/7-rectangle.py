#!/usr/bin/python3
"""This module defines rectangle class"""


class Rectangle:
    """This class defines a Rectangle and it's properties
        Args:
            __width: private attribute
            __height: private property for the rectangle
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """initial constructor function for the rectangle class"""
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Getter property of the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter property for the width which checks"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter property of the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter property for the height which checks"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """returns the perimeter of the rectangle"""
        return (2 * self.__height) + (2 * self.__width)

    def __str__(self):
        """print the rectangle with the character #"""
        if self.__height == 0 or self.__width == 0:
            return ""
        rect = []
        for col in range(self.__height):
            for row in range(self.__width):
                rect.append(str(Rectangle.print_symbol))
            if col != self.__height - 1:
                rectobj.append('\n')
        return "".join(rect)

    def __repr__(self):
        """Return the representation of the class using the eval() function"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        del self
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
