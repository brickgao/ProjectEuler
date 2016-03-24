#!/bin/env python3
# -*- coding: utf-8 -*-

import math
import functools


@functools.lru_cache(maxsize=None)
def is_squares(num):
    approximate = math.floor(math.sqrt(num)) - 1
    for i in range(approximate, approximate + 4):
        if i ** 2 == num:
            return True
    return False


@functools.lru_cache(maxsize=None)
def is_int(num):
    return int(num) == num


def solve():
    a, square_a = 1, 1
    while True:
        b, square_b = 1, 1
        while b < a:
            square_f = square_a - square_b
            if not is_squares(square_f):
                b, square_b = b + 1, (b + 1) ** 2
                continue
            c, square_c = 1, 1
            while c < b:
                square_d = square_b - square_c
                square_e = square_a - square_c
                if is_squares(square_d) and is_squares(square_e):
                    x = (square_a + square_d) / 2.
                    y = square_b - x
                    z = square_c - y
                    if (
                        y > 0 and z > 0 and
                        is_int(x) and is_int(y) and is_int(z)
                    ):
                        return int(x + y + z)
                c, square_c = c + 1, (c + 1) ** 2
            b, square_b = b + 1, (b + 1) ** 2
        a, square_a = a + 1, (a + 1) ** 2


if __name__ == "__main__":
    print(solve())
