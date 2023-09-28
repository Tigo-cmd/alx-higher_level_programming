#!/usr/bin/python3
"""This is a Rectangle class with basic attributes"""


from models.base import Base


class Rectangle(Base):
    """This Creates a Rectangle Class
    Args:
        Width: private instance attribute sets the width
        Height:private instance attribute sets the height
        X:
        Y:
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """This is the default constructor for the rectangle class"""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """getter function for the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter function for the width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """getter function for the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter function for the height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """getter function for the x"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter function for the x"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """getter function for the y"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter function for the y"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """this returns the area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """prints to stdout the Rectangle
        instance with the character #
        """
        if self.__height == 0 or self.__width == 0:
            print("")
            return
        [print("") for y in range(self.__y)]
        for i in range(self.height):
            [print(" ", end="") for x in range(self.__x)]
            [print("#", end="") for j in range(self.__width)]
            print("")

    def __str__(self):
        """this returns [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        return f"{self.__class__.__name__} ({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}"

    def update(self, *args):
        """assigns an argument to each attribute:"""
        if args and len(args) != 0:
            argc = 0
            for arg in args:
                if argc == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif argc == 1:
                    self.width = arg
                elif argc == 2:
                    self.__height = arg
                elif argc == 3:
                    self.x = arg
                elif argc == 4:
                    self.y = arg
                argc += 1
        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle:"""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
