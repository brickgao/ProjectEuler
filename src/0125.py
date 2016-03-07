#!/bin/env python3
# -*- coding: utf-8 -*-

import math


def solve():
    rec, limit = set(), 10 ** 8
    for i in range(1, int(math.sqrt(limit)) + 1):
        tmp, j = i * i, i
        while tmp < limit:
            j += 1
            tmp += j * j
            if tmp < limit and str(tmp) == str(tmp)[::-1]:
                rec.add(tmp)
    return sum(rec)


if __name__ == "__main__":
    print(solve())
