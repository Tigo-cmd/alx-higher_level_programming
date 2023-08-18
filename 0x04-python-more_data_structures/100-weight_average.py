#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    run_sum = 0
    nd_elem = 0
    for i in my_list:
        for j in i:
            run_sum += i[-1] * i[-2]
            nd_elem += i[-1]
    return run_sum / nd_elem
