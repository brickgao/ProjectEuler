# !/bin/env python2
# -*- coding: utf-8 -*-

import math
import urllib


def solve():
    response = urllib.urlopen(
        "https://projecteuler.net/project/resources/p099_base_exp.txt"
    )
    line, cnt = response.readline(), 1
    result, maxn = 0, 0
    while line != "":
        line = line[:-1] if line.endswith("\n") else line
        num1, num2 = map(int, line.split(","))
        _num = num2 * math.log(num1)
        if _num > maxn:
            result, maxn = cnt, _num
        line, cnt = response.readline(), cnt + 1
    return result


if __name__ == "__main__":
    print solve()
