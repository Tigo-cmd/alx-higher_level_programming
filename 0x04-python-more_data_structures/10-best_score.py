#!/usr/bin/python3
def best_score(a_dictionary):
    j = 0
    upper = 0
    if not a_dictionary:
        return None
    else:
        num = list(a_dictionary.values())
        init = list(a_dictionary.keys())
        upper = max(num)
        for i in range(len(num)):
            if num[i] == upper:
                j = i
        return init[j]
