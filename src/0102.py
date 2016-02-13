# !/bin/env python2
# -*- coding: utf-8 -*-

import urllib


def cross_mul(p1, p2):
    return p1[0] * p2[1] - p1[1] * p2[0]


def solve():
    response = urllib.urlopen(
        "https://projecteuler.net/project/resources/p102_triangles.txt"
    )
    line, result = response.readline(), 0
    while line != "":
        line = line[:-1] if line.endswith("\n") else line
        x1, y1, x2, y2, x3, y3 = map(int, line.split(","))
        _tmp1 = (cross_mul((x2 - x1, y2 - y1), (-x1, -y1)) *
                 cross_mul((x3 - x1, y3 - y1), (-x1, -y1)))
        _tmp2 = (cross_mul((x3 - x2, y3 - y2), (-x2, -y2)) *
                 cross_mul((x1 - x2, y1 - y2), (-x2, -y2)))
        if _tmp1 <= 0 and _tmp2 <= 0:
            result += 1
        line = response.readline()
    return result


if __name__ == "__main__":
    print solve()
