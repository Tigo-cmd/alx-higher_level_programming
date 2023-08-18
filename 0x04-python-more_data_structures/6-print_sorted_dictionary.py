#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    key_list = []
    for i in sorted(a_dictionary):
        key_list.append(i)
    for j in key_list:
        print("{}: {}".format(j, a_dictionary.get(j)))
