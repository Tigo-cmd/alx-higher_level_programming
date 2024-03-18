#!/usr/bin/python3
def element_at(my_list, idx):
    l = len(my_list)
    if idx < 0:
        return "None"
    i = 0
    while i != l:
        if i == idx:
            return my_list[i]
        i = i + 1
