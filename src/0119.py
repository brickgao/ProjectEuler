#!/bin/env python3
# -*- coding: utf-8 -*-


def solve():
    l = []
    for i in range(2, 100):
        for j in range(2, 10):
            num = int(i ** j)
            if sum(map(int, str(num))) == i:
                l.append(num)
    l.sort()
    assert l[9] == 614656
    return l[29]


if __name__ == "__main__":
    print(solve())
