# !/bin/env python2
# -*- coding: utf-8 -*-


def solve():
    minn, result, target = 2000000, -1, 2000000
    x, y = 2000, 1
    while x >= y:
        now = x * (x + 1) * y * (y + 1) / 4
        if minn > abs(now - target):
            minn, result = abs(now - target), x * y
        if now > target:
            x -= 1
        else:
            y += 1
    return result


if __name__ == "__main__":
    print solve()
