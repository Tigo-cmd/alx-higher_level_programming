#!/usr/bin/python3
"""This is the base class all clases inherits frorm here"""


class Base:
    """This is the base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """this is the default constructor for the base class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """static method def to_json_string(list_dictionaries):
        that returns the JSON string representation of list_dictionaries:
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set:"""
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new_class = cls(1, 1)
            else:
                new_class = cls(1)
            new_class.update(**dictionary)
            return new_class

    @classmethod
    def save_to_file(cls, list_objs):
        """class method def save_to_file(cls, list_objs): that writes
        the JSON string representation of list_objs to a file
        """
        with open(f"{cls.__name__}.json", 'w') as file:
            if list_objs is None:
                file.write("[]")
            else:
                main_list = [i.to_dictonary() for i in list_objs]
                file.write(Base.to_json_string(main_list))

    @staticmethod
    def from_json_string(json_string):
        """ returns the list of the JSON string representation json_string:"""
        if json_string is None or json_string == []:
            return []
        return json.loads(json_string)   

    @classmethod
    def load_from_file(cls):
        """list of instances"""
        file = str(cls.__name__) + ".json"
        try:
            with open(file, "r") as json_file:
                main_list = Base.from_json_string(json_file.read())
                return [cls.create(**d) for d in main_list]
        except IOError:
            return []
