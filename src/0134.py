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


def get_prime(n):
    result = [2]
    for i in range(3, n + 1, 2):
        if is_probably_prime(i):
            result.append(i)
    return result


def extgcd(a, b):
    x, last_x = 0, 1
    y, last_y = 1, 0
    while b != 0:
        x, last_x = last_x - (a // b) * x, x
        y, last_y = last_y - (a // b) * y, y
        a, b = b, a % b
    return last_x, last_y


def solve():
    limit = 10 ** 6
    primes, result = get_prime(limit + 100), 0
    for i in range(2, len(primes) - 1):
        p1, p2 = primes[i], primes[i + 1]
        if p1 > limit:
            break
        step = 10 ** len(str(p1))
        x, y = extgcd(step, p2)
        x = (x * (p2 - p1) % p2 + p2) % p2
        result += x * step + p1
    return result


if __name__ == "__main__":
    print(solve())
