# -*- coding: utf-8 -*-
# !/bin/env python2

from math import sqrt


def cnt_prime(num):
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return 0
    return 0 if num == 1 else 1


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
