#!/bin/env python3
# -*- coding: utf-8 -*-


def solve():
    result, limit = 0, 10 ** 6
    outer_upper_bound = limit // 4 + 2
    for outer in range(3, outer_upper_bound):
        for inner in range(outer - 2, 0, -2):
            if outer ** 2 - inner ** 2 > limit:
                break
            result += 1
    return result


if __name__ == "__main__":
    print(solve())
