#!/bin/env python3
# -*- coding: utf-8 -*-

import math


def solve():
    limit, rec = 10 ** 12, set()
    for a in range(2, 10 ** 4):
        for b in range(1, a):
            if (a ** 3) * b + (b ** 2) >= limit:
                break
            if math.gcd(a, b) > 1:
                continue
            c = 1
            while True:
                n = (a ** 3) * b * (c ** 2) + c * (b ** 2)
                if n >= limit:
                    break
                if int(math.sqrt(n)) ** 2 == n and n not in rec:
                    rec.add(n)
                c += 1
    return sum(rec)


if __name__ == "__main__":
    print(solve())
