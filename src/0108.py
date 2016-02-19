#!/bin/env python2
# -*- coding: utf-8 -*-

import math


def get_primes():
    limit, result = 200000, []
    for i in range(2, limit):
        tag = True
        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0:
                tag = False
                break
        if tag:
            result.append(i)
    return result


def solve():
    primes, num, limit = get_primes(), 4, 1000
    while True:
        remain, combinations_cnt, now = num, 1, 0
        while remain != 1:
            cnt = 1
            while remain % primes[now] == 0:
                remain, cnt = remain / primes[now], cnt + 2
            combinations_cnt *= cnt
            now += 1
        if (combinations_cnt + 1) / 2 > limit:
            return num
        num += 1


if __name__ == "__main__":
    print solve()
