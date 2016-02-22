#!/bin/env python3
# -*- coding: utf-8 -*-

import random
from functools import lru_cache


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


@lru_cache(maxsize=None)
def generate_strs(n, d, cnt):
    if n == 0:
        return [""]
    elif cnt == n:
        return [str(d) * cnt]
    else:
        result = []
        for i in range(10):
            for nxt in generate_strs(n - 1, d, cnt - (1 if i == d else 0)):
                result.append(str(i) + nxt)
        return result


@lru_cache(maxsize=None)
def generate_primes(n, d, cnt):
    result = []
    for num in generate_strs(n, d, cnt):
        if not num.startswith("0") and is_probably_prime(int(num)):
            result.append(int(num))
    return result


@lru_cache(maxsize=None)
def get_m(n, d):
    for cnt in range(n, 0, -1):
        if len(generate_primes(n, d, cnt)) > 0:
            break
    return cnt


@lru_cache(maxsize=None)
def get_n(n, d):
    return len(generate_primes(n, d, get_m(n, d)))


@lru_cache(maxsize=None)
def get_s(n, d):
    return sum(generate_primes(n, d, get_m(n, d)))


def solve():
    result, n = 0
    for d in range(10):
        _sum = get_s(n, d)
        print(d, get_m(n, d), get_n(n, d), _sum)
        result += _sum
    return result


if __name__ == "__main__":
    print(solve())
