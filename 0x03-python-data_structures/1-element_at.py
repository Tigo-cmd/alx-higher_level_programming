#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return None
        exit()
    if idx > len(my_list):
        return None
        exit()
    for i in range(0, len(my_list)):
        if i == idx:
            return my_list[i]
