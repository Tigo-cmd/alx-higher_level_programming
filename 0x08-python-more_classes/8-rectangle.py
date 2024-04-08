#!/usr/bin/python3
"""rectangle class module that defines a Rectangle class"""


class Rectangle:
    """This class defines a rectangle and instanciates it for life"""
    number_of_instances = 0  # public instance attributes
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ instance method
            Args:
                width: private instance attribute
                height: private instance attribute
        """
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """getter method for width"""
        return self.__width

    @property
    def height(self):
        """getter property for rectangle height"""
        return self.__height

    @width.setter
    def width(self, value):
        """setter property for rectangle width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """setter property for rectangle height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """RETURNS the area of th rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """returns the perimeter of the rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """prints the string rep of the Rectangle.print_symbol"""
        if self.__height == 0 or self.__width == 0:
            return ""
        else:
            main = []
            for i in range(self.height):
                main.append(str(self.print_symbol) * self.__width)
                if i != self.__height - 1:
                    main.append("\n")
            return "".join(main)

    def __repr__(self):
        """return a string representation of the rectangle"""
        main = f"Rectangle({self.__width}, {self.__height})"
        return main

    def __del__(self):
        """detects instance deletion"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns the biggest rectangle based on area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return rect_2
        else:
            return rect_1
