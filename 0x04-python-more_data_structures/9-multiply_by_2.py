#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = a_dictionary.copy()
    for i in a_dictionary:
        mul = a_dictionary.get(i) * 2
        new_dict[i] = mul
    return new_dict
