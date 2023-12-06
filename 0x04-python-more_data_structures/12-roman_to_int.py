#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    else:
        roman_figure = {
                'I': 1,
                'V': 5,
                'X': 10,
                'L': 50,
                'C': 100,
                'D': 500,
                'M': 1000
                }
        res = 0
        prev = 0

        for number in reversed(roman_string):
            value = roman_figure.get(number, 0)
            if value < prev:
                res -= value
            else:
                res += value
            prev = value
        return res
