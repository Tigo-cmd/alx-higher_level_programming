#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    max_item = next(iter(a_dictionary))
    for i in a_dictionary:
        if a_dictionary.get(i) > a_dictionary.get(max_item):
            max_item = i
    return max_item
