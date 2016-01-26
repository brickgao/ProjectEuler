# !/bin/env python2
# -*- coding: utf-8 -*-


def solve():
    phi = [i for i in range(1000001)]
    for i in range(2, 1000001):
        if phi[i] == i:
            for k in range(i, 1000001, i):
                phi[k] -= phi[k] // i
    return sum(phi) - 1


if __name__ == "__main__":
    print solve()
