#!/bin/env python3
# -*- coding: utf-8 -*-

import math
import random
import itertools


def is_probably_prime(n, k=10):
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


def is_squarefree(num):
    if not is_probably_prime(num):
        upper_bound = int(math.sqrt(num)) + 1
        for i in itertools.chain([2], range(3, upper_bound, 2)):
            cnt = 0
            while num % i == 0:
                num, cnt = num / i, cnt + 1
            if cnt >= 2:
                return False
    return True


def solve():
    nums = set([1])
    pre, limit = [1, 1], 51
    for level in range(limit - 2):
        now = [1] + [pre[i] + pre[i + 1] for i in range(len(pre) - 1)] + [1]
        nums, pre = nums | set(now), now
    return sum(filter(is_squarefree, nums))


if __name__ == "__main__":
    print(solve())
