#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    else:
        high = my_list[0]
        for i in range(0, len(my_list)):
            if my_list[i] > high:
                high = my_list[i]
        return high
