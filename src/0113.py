#!/bin/env python3
# -*- coding: utf-8 -*-


def solve():
    N, n = 120, 100
    c = [[0 for i in range(N + 1)] for j in range(N + 1)]
    for i in range(N + 1):
        c[i][0] = c[i][i] = 1
        for j in range(1, i):
            c[i][j] = c[i - 1][j] + c[i - 1][j - 1]
    return c[n + 10][10] + c[n + 9][9] - 10 * n - 2


if __name__ == "__main__":
    print(solve())
