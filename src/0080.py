# !/bin/env python2
# -*- coding: utf-8 -*-

from decimal import getcontext, Decimal


def solve():
    total, getcontext().prec = 0, 102
    for num in range(1, 101):
        num_sqrt = Decimal(num).sqrt()
        if int(num_sqrt) ** 2 == num:
            continue
        total += sum(map(int, str(int(num_sqrt * (10 ** 100))))[:100])
    return total


if __name__ == "__main__":
    print solve()
