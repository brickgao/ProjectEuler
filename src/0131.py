#!/bin/env python3
# -*- coding: utf-8 -*-

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
    limit = 1000000
    i, result = 1, 0
    while True:
        now, i = int((i + 1) ** 3 - i ** 3), i + 1
        if now > limit:
            break
        result += 1 if is_probably_prime(now) else 0
    return result


if __name__ == "__main__":
    print(solve())
