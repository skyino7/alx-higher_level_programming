#!/usr/bin/python3
"""
Create a function that converts a Roman numeral to an integer.
"""


def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman_val = {'I': 1,
                 'V': 5,
                 'X': 10,
                 'L': 50,
                 'C': 100,
                 'D': 500,
                 'M': 1000
                 }

    res = 0
    val = 0

    for char in roman_string[::-1]:
        value = roman_val.get(char, 0)

        if value < val:
            res -= value
        else:
            res += value

        val = value

    return res
