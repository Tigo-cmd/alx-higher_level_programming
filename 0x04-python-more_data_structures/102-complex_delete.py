#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for i in list(a_dictionary):
        if a_dictionary.get(i) == value:
            del a_dictionary[i]
    return a_dictionary
