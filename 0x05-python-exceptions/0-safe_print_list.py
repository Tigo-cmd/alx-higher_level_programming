#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    try:
        for j in my_list:
            if i == x:
                break
            else:
                print(j, end="")
            i += 1
        print()
        return i
    except TypeError:
        pass
