#!/bin/env python3
# -*- coding: utf-8 -*-

from collections import defaultdict


def solve():
    result, limit = 0, 10 ** 6
    outer_upper_bound, rec = limit // 4 + 2, defaultdict(lambda: 0)
    for outer in range(3, outer_upper_bound):
        for inner in range(outer - 2, 0, -2):
            tiles = outer ** 2 - inner ** 2
            if tiles > limit:
                break
            rec[tiles] += 1
    for key in rec:
        if 1 <= rec[key] <= 10:
            result += 1
    return result


if __name__ == "__main__":
    print(solve())
