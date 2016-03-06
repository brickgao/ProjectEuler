#!/bin/env python3
# -*- coding: utf-8 -*-

import math


def get_prime(n):
    result = [2]
    for i in range(3, n + 1):
        tag = True
        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0:
                tag = False
                break
        if tag:
            result.append(i)
    return result


def solve():
    rec, upper_bound = [], 100000
    primes = get_prime(upper_bound)
    for i in range(1, upper_bound + 1):
        tmp, now = 1, i
        for prime in primes:
            if prime > now:
                break
            if now % prime == 0:
                while now % prime == 0:
                    now /= prime
                tmp *= prime
        rec.append((tmp, i))
    rec.sort()
    return rec[10000 - 1][1]


if __name__ == "__main__":
    print(solve())
