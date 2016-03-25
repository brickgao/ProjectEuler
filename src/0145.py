#!/bin/env python3
# -*- coding: utf-8 -*-


def solve():
    result = 0
    for i in range(1, 10):
        if i % 4 == 3:
            result += 100 * 500 ** int(i / 4)
        elif i % 2 == 0:
            result += 20 * 30 ** int(i / 2 - 1)
    return int(result)


if __name__ == "__main__":
    print(solve())
