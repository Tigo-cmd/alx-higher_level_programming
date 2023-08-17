#!/usr/bin/python3
def uniq_add(my_list=[]):
    added = 0
    new_list = []
    for i in my_list:
        if i not in new_list:
            new_list.append(i)
    for j in new_list:
        added += j
    return added
