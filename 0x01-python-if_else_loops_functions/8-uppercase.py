#!/usr/bin/python3
def uppercase(str):
    for i in str:
        j = ord(i)
        print("{}".format(chr(ord(i) - 32)) if j >= 97 <= 122 else "{}".format(i), end="")
    print()
