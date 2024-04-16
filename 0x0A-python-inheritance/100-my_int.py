#!/usr/bin/python3
"""defines a rebel class module thats rebels int class"""


class MyInt(int):
    """this class inherits from the int class it's a rebel
     	MyInt is a rebel. MyInt has == and != operators inverted
    """

    def __init__(self, num):
        """initialization rebel function"""
        super().__init__()
        self.__num = num

    def __eq__(self, other):
        """implements the inverted function"""
        if self.__num == other:
            return False
        return True

    def __ne__(self, other):
        """implements the rebel of __eq__()"""
        if self.__num != other:
            return False
        return True
