#!/bin/env python3
# -*- coding: utf-8 -*-


def solve():
    result, limit = 0, 10 ** 7
    rec, upper_bound = [0 for i in range(limit)], limit // 2
    for factor in range(2, upper_bound):
        for num in range(factor, limit, factor):
            rec[num] += 1
    print("done")
    for num in range(2, limit):
        if rec[num] == rec[num - 1]:
            result += 1
    return result


if __name__ == "__main__":
    print(solve())
