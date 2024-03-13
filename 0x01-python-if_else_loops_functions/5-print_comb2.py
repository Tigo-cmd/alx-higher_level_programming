#!/usr/bin/python3
for i in range(99):
    print("0{}, ".format(i) if i < 10 else "{}, ".format(i), end="")
print("99")

