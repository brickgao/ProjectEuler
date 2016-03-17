#!/bin/env python3
# -*- coding: utf-8 -*-


def solve():
    limit = 10 ** 6
    rec = [0 for i in range(limit + 1)]
    for u in range(1, limit):
        v = 1
        while u * v <= limit:
            if (u + v) % 4 == 0 and 3 * v - u > 0 and (3 * v - u) % 4 == 0:
                rec[u * v] += 1
            v += 1
    return sum(map(lambda x: x == 10, rec))


if __name__ == "__main__":
    print(solve())
