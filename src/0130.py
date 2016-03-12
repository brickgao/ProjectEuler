#!/bin/env python3
# -*- coding: utf-8 -*-

import math
import random


def is_probably_prime(n, k=20):
    if n <= 3:
        return [False, False, True, True][n]
    else:
        s, d, x = 0, n - 1, 0
        while d % 2 == 0:
            s, d = s + 1, d >> 1
        for i in range(k):
            a = random.randrange(2, n)
            x = pow(a, d, n)
            if x == 1:
                continue
            tag = False
            for j in range(s - 1):
                if x == n - 1:
                    tag = True
                    break
                x = x * x % n
            if tag:
                continue
            else:
                if x != n - 1:
                    return False
        return True


def solve():
    n, limit, result_l = 3, 25, []
    while True:
        if math.gcd(n, 10) == 1 and not is_probably_prime(n):
            now, cnt = 1, 1
            while now != 0:
                now, cnt = (now * 10 + 1) % n, cnt + 1
            if (n - 1) % cnt == 0:
                result_l.append(n)
        if len(result_l) >= limit:
            break
        n += 2
    return sum(result_l)


if __name__ == "__main__":
    print(solve())
