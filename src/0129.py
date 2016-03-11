#!/bin/env python3
# -*- coding: utf-8 -*-

import math


def solve():
    n, limit = 1000001, 1000000
    while True:
        if math.gcd(n, 10) == 1:
            now, cnt = 1, 1
            while now != 0:
                now, cnt = (now * 10 + 1) % n, cnt + 1
        if cnt > limit:
            return n
        n += 2


if __name__ == "__main__":
    print(solve())
