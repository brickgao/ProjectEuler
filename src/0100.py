# !/bin/env python2
# -*- coding: utf-8 -*-


def solve():
    # http://math.stackexchange.com/questions/75031/solving-quadratic-diophantine-equations
    # http://mathworld.wolfram.com/PellEquation.html
    limit, x, y = 10 ** 12, 1, 1
    while y <= limit:
        x, y = 3 * x + 2 * y - 2, 4 * x + 3 * y - 3
    return x


if __name__ == "__main__":
    print solve()
