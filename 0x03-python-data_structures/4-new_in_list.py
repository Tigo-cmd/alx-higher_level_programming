#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    newlist = my_list[:]
    if idx < 0:
        return newlist
    if idx > len(my_list):
        return newlist
    for i in range(0, len(my_list)):
        if i == idx:
            newlist[i] = element
    return newlist
