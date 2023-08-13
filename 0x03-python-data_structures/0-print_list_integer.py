#!/usr/bin/python3
def print_list_integer(my_list=[]):
    for i in my_list:
        try:
            print("{:d}".format(i))
        except ValueError:
            continue
