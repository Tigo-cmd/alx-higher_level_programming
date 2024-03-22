#!/usr/bin/python3
def uppercase(str):
    new_list = []
    for word in str:
        print(chr(ord(word) - 32), end="" if 92 <= ord(word) <= 122 else word)
    print()
