# -*- coding: utf-8 -*-
# !/bin/env python2

from fractions import Fraction


def get_e(num):
    now = Fraction(1 if num % 3 else num // 3 * 2, 1)
    for i in range(num - 1, 1, -1):
        tmp = 1 if i % 3 else i // 3 * 2
        now = tmp + 1 / now
    now = 2 + 1 / now
    return now if num > 1 else 2


if __name__ == "__main__":
    print sum(map(int, str(get_e(100).numerator)))
