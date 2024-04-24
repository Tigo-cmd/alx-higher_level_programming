#!/usr/bin/python3
"""Defines a Rectangle class"""
import args

from models.base import Base


class Rectangle(Base):
    """this class inherits from base for functionalities"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initializing function
        ARgs:
            id: set to the id of the super class
            width: private instance attribute of the class
            height: private instance attribute of the class
            x: private instance attribute for positions
            y: private instance attribute for positions
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """getter property for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter attrib for width"""
        if not isinstance(value, int):
            raise TypeError(f"width must be an integer")
        elif value <= 0:
            raise ValueError(f"width must be > 0")
        self.__width = value

    @property
    def height(self):
        """getter prop for height"""
        return self.__width

    @height.setter
    def height(self, value):
        """setter property for height"""
        if not isinstance(value, int):
            raise TypeError(f"height must be an integer")
        elif value <= 0:
            raise ValueError(f"height must be > 0")
        else:
            self.__width = value

    @property
    def x(self):
        """getter property for x attrib"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter prop for x attrib"""
        if not isinstance(value, int):
            raise TypeError(f"x must be an integer")
        elif value < 0:
            raise ValueError(f"x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """getter property for y attrib"""
        return self.__y

    @y.setter
    def y(self, value):
        """set property fo y function"""
        if not isinstance(value, int):
            raise TypeError(f"y must be an integer")
        elif value < 0:
            raise ValueError(f"y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """defines the area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """prints in stdout the Rectangle instance with the character
        # - you don’t need to handle x and y here
        """
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)

    def __str__(self):
        """overriding the __str__ method so that it returns
        [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}"

    def update(self, *args):
        """assigns an argument to each attribute
        Args:
            args: variable list of arguments
        """
        if args and len(args) != 0:
            counter = 0
            for arg in args:
                if counter == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif counter == 1:
                    self.width = arg
                elif counter == 2:
                    self.__height = arg
                elif counter == 3:
                    self.x = arg
                elif counter == 4:
                    self.y = arg
                counter += 1

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle:"""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }