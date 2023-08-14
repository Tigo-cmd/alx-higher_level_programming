#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = []
    for i in my_list:
        j = i % 2
        new_list.append(j == 0)
    return new_list
