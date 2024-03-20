#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    j = 0
    tuple_a = list(tuple_a)
    tuple_b = list(tuple_b)
    if len(tuple_a) == 0:
        for i in range(2):
            tuple_a.append(0)
    elif len(tuple_b) == 0:
        for i in range(2):
            tuple_b.append(0)
    elif len(tuple_a) < 2:
        tuple_a.append(j)
    elif len(tuple_b) < 2:
        tuple_b.append(j)

    a, b = tuple(tuple_a)
    c, d = tuple(tuple_b)
    new = (a + c, b + d)
    return new[:2]
