#!/usr/bin/python3
"""This is square class that inherits for the rectangle class """


from models.rectangle import Rectangle


class Square(Rectangle):
    """This is a square class that inherits form the rectangle class

    Args:
        size: size of the square
    """

    def __init__(self, size, x=0, y=0, id=None):
        """default constructor for square class"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """overloading method which returns
        [Square] (<id>) <x>/<y> - <size> - width or height
        """
        ret = f"[{self.__class__.__name__}] "
        ret += f"({self.id}) {self.__x}/{self.__y}"
        ret += f" - {self.size}"
        return ret

    @property
    def size(self):
        """return the size of the square"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """assigns attributes"""
        if args and len(args) != 0:
            argc = 0
            for arg in args:
                if argc == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif argc == 1:
                    self.size = arg
                elif argc == 3:
                    self.x = arg
                elif argc == 4:
                    self.y = arg
                argc += 1
        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.width = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle:"""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }
