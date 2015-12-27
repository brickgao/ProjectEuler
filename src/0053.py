# -*- coding: utf-8 -*-
# !/bin/env python2


def solve():
    c = [[0 for i in range(101)] for j in range(101)]
    for i in range(101):
        c[i][0] = c[i][i] = 1
        for j in range(i):
            c[i][j] = c[i - 1][j] + c[i - 1][j - 1]
    result = 0
    for i in range(101):
        result += len(filter(lambda x: x > 1000000, c[i]))
    return result


if __name__ == "__main__":
    print solve()
