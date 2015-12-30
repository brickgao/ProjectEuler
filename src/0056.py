# -*- coding: utf-8 -*-
# !/bin/env python2


def solve():
    result = 0
    for a in range(1, 100):
        for b in range(1, 100):
            num = map(int, str(a ** b))
            result = max(sum(num), result)
    return result


if __name__ == "__main__":
    print solve()
