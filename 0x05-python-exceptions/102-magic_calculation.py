#!/usr/bin/python3
def magic_calculation(a, b):
    new = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            new += a ** b / 1
        except Exception:
            new = b + a
            break
    return new
