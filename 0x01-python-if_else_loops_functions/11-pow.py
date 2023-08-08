#!/usr/bin/python3
def pow(a, b):
    if b == 0:
        return 1
    elif b > 0:
        power = 1
        for _ in range(b):
            power = power * a
        return power
    else:
        return 1 / pow(a, -b
