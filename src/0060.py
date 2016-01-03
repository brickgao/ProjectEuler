# -*- coding: utf-8 -*-
# !/bin/env python2

import random
import itertools
from math import sqrt


primes = []
is_prime = [True for i in range(10000)]


def check_prime(num):
    if num % 2 == 0:
        return False
    for i in range(3, int(sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return False if num == 1 else True


def get_prm(n):
    i, k, e = 0, 0, int(sqrt(n) + 1)
    primes.append(2)
    is_prime[0] = is_prime[1] = False
    for i in range(4, n, 2):
        is_prime[i] = False
    for i in range(3, e, 2):
        if is_prime[i]:
            primes.append(i)
            s, j = i * 2, i * i
            while j < n:
                is_prime[j] = False
                j += s
    while i < n:
        if is_prime[i]:
            primes.append(i)
        i += 2


def all_prime(l):
    return all(check_prime(int(str(p[0]) + str(p[1])))
               for p in itertools.permutations(l, 2))


def dfs(l):
    if len(l) == 5:
        return l
    for p in primes:
        if p > l[-1] and all_prime(l + [p]):
            nxt_l = dfs(l + [p])
            if nxt_l:
                return nxt_l
    return []


def solve():
    get_prm(10000)
    result = []
    while not result:
        result = dfs([primes.pop(0)])
    print result, sum(result)
    return sum(result)


if __name__ == "__main__":
    solve()
