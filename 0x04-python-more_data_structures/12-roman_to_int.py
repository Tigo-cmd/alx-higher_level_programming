#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0
    numerals = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    final = 0
    initial = 0
    for num in reversed(roman_string):
        pair = numerals[num]
        if pair >= initial:
            final = final + pair
        else:
            final = final - pair
        initial = pair
    return final
