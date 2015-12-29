# -*- coding: utf-8 -*-
# !/bin/env python2


def solve():
    result = 0
    for num in range(10000):
        _num, tag = num, False
        for i in range(50):
            _num += int(str(_num)[::-1])
            if str(_num) == str(_num)[::-1]:
                tag = True
                break
        if not tag:
            result += 1
    return result


if __name__ == "__main__":
    print solve()
