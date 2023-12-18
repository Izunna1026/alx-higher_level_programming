#!/usr/bin/python3
def magic_calculation(a, b):
    inp = 0
    for val in range(1, 3):
        try:
            if val > a:
                raise Exception('Too far')
            inp += a ** b / val
        except Exception:
            inp = b + a
            break
    return inp
