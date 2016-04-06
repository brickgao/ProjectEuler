#!/bin/env python3
# -*- coding: utf-8 -*-


def solve():
    n, late_limit, consec_absent_limit = 30 + 1, 1 + 1, 2 + 1
    line = [0] * late_limit
    rec = [
        [line[:] for i in range(consec_absent_limit)] for j in range(n)
    ]
    rec[0][0][0] = 1
    for i in range(1, n):
        for j in range(consec_absent_limit):
            for k in range(late_limit):
                if j == 0:
                    for m in range(consec_absent_limit):
                        rec[i][j][k] += rec[i - 1][m][k]
                    if k != 0:
                        for m in range(consec_absent_limit):
                            rec[i][j][k] += rec[i - 1][m][k - 1]
                else:
                    rec[i][j][k] += rec[i - 1][j - 1][k]
    return sum(map(sum, rec[n - 1]))


if __name__ == "__main__":
    print(solve())
