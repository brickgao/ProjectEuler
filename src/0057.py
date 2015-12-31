# -*- coding: utf-8 -*-
# !/bin/env python2

from fractions import Fraction


def solve():
    num, result = Fraction(1, 1), 0
    for i in range(1000):
        num = 1 + 1 / (1 + num)
        if len(str(num.numerator)) > len(str(num.denominator)):
            result += 1
    return result


if __name__ == "__main__":
    print solve()
