#!/bin/env python3
# -*- coding: utf-8 -*-


def get_total(n):
    return (n + 1) * n // 2


def solve():
    result, limit, module = 0, 10 ** 9, 7
    product, now, rec = 1, limit, []
    while now > 0:
        rec = [now % module] + rec
        now //= module
    for i in range(len(rec)):
        n = len(rec) - i - 1
        result += product * get_total(rec[i]) * (get_total(7) ** n)
        product *= rec[i] + 1
    return result


if __name__ == "__main__":
    print(solve())
