#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    new_keys = list(a_dictionary.keys())
    new_keys.sort()

    for o in new_keys:
        print(f"{o}: {a_dictionary[o]}")
