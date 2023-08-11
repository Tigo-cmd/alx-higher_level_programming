#!/usr/bin/python3
def remove_char_at(str, n):
    for i in range(0, len(str)):
        if i == n:
            continue
        str += str[i]
    return str[i + 1:]
