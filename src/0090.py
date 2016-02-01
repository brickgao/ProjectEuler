# !/bin/env python2
# -*- coding: utf-8 -*-

from itertools import combinations


def solve():
    cube = list(combinations([0, 1, 2, 3, 4, 5, 6, 7, 8, 6], 6))
    squares = [(0, 1), (0, 4), (0, 6), (1, 6), (2, 5), (3, 6), (4, 6), (8, 1)]
    result = 0
    for i in range(len(cube)):
        for j in range(i + 1, len(cube)):
            if all(x in cube[i] and y in cube[j] or
                   x in cube[j] and y in cube[i] for x, y in squares):
                result += 1
    return result


if __name__ == "__main__":
    print solve()
