#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    try:
        for i in range(0, list_length):
            if my_list_2[i] == 0 or my_list_1[i] == 0:
                print("division by 0")
                new_list.append(0)
                continue
            if not isinstance(my_list_2[i], int) or not isinstance(my_list_2[i], int):
                print("wrong type")
                new_list.append(0)
                continue
            new_list.append(my_list_1[i] / my_list_2[i])
    except (TypeError, ZeroDivisionError, IndexError):
        if IndexError:
            print("out of range")
            new_list.append(0)
    return new_list
