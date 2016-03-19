#!/bin/env python3
# -*- coding: utf-8 -*-


def solve():
    limit, fibs = 15, [0, 1, 1]
    for i in range(limit * 2):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs[limit * 2] * fibs[limit * 2 + 1]


if __name__ == "__main__":
    print(solve())
