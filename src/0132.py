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
    primes = get_prime(200000)
    result, i = [], 0
    while len(result) < 40:
        if pow(10, 10 ** 9, 9 * primes[i]) == 1:
            result.append(primes[i])
        i += 1
    return sum(result)


if __name__ == "__main__":
    print(solve())
