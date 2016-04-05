#!/bin/env python3
# -*- coding: utf-8 -*-


def solve():
    now, a, b, mod = 1, 1777, 1855, 10 ** 8
    for i in range(b):
        now = pow(a, now, mod)
    return now


if __name__ == "__main__":
    print(solve())
