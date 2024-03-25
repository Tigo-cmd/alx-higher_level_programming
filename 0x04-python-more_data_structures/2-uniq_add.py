#!/usr/bin/python3
def uniq_add(my_list=[]):
    new = []
    for i in my_list:
        if i in new:
            continue
        new.append(i)
    return sum(new)
