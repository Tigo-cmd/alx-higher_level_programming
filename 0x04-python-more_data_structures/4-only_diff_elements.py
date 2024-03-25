#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    new = []
    for i in set_1:
        if i not in set_2:
            new.append(i)
    for i in set_2:
        if i not in set_1:
            new.append(i)
    return set(new)
