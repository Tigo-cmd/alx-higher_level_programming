#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for i in my_list[::-1]:
        try:
            print("{:d}".format(i))
        except ValueError:
            continue
