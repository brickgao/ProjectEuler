# -*- coding: utf-8 -*-
# !/bin/env python2

import math


def solve():
    rec = [0 for i in range(12001)]
    for i in range(1, 12001):
        if i <= 3:
            rec[i] = 0
        else:
            rec[i] += int(math.floor(i / 2.)) - int(math.ceil(i / 3.)) + 1
            rec[i] -= len(filter(lambda x: x, [i % 2 == 0, i % 3 == 0]))
        for j in range(2 * i, 12001, i):
            rec[j] -= rec[i]
    return sum(rec)


if __name__ == "__main__":
    print solve()
