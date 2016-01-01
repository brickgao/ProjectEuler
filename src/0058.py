# -*- coding: utf-8 -*-
# !/bin/env python2

import random
from math import sqrt


def cnt_prime(num):
    if is_probably_prime(num):
        for i in range(2, int(sqrt(num)) + 1):
            if num % i == 0:
                return 0
        return 0 if num == 1 else 1
    else:
        return 0


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
    cnt, now = 0, 1
    while True:
        now += 2
        r_d_number = now * now
        l = [
            r_d_number - (now - 1) * 3,
            r_d_number - (now - 1) * 2,
            r_d_number - (now - 1) * 1,
            r_d_number
        ]
        cnt += sum(map(cnt_prime, l))
        if float(cnt) / float((now // 2) * 4 + 1) < 0.1:
            return now


if __name__ == "__main__":
    print solve()
