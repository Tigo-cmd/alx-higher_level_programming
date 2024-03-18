#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if not abs(idx):
        return my_list
    new_list = my_list.copy()
    i = 0
    while i != len(new_list):
        if i == idx:
            new_list[i] = element
        i = i + 1
    return new_list

