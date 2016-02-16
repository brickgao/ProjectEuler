# !/bin/env python2
# -*- coding: utf-8 -*-

import math
import urllib
from itertools import combinations


def solve():
    response = urllib.urlopen(
        "https://projecteuler.net/project/resources/p105_sets.txt"
    )
    line, result = response.readline(), 0
    while line != "":
        line = line[:-1] if line.endswith("\n") else line
        array = sorted(map(int, line.split(",")))
        length, tag, _sum1, _sum2 = len(array), True, array[0], 0
        for i in range(int(math.ceil(length / 2))):
            _sum1, _sum2 = _sum1 + array[i + 1], _sum2 + array[length - i - 1]
            if _sum1 <= _sum2:
                tag = False
                break
        if len(set(array)) != length:
            tag = False
        if tag:
            for length1 in range(length):
                for c1 in combinations(array, length1 + 1):
                    _nxt = set(array) - set(c1)
                    _nxt_len = len(_nxt)
                    _sum1 = sum(c1)
                    for length2 in range(_nxt_len):
                        for c2 in combinations(_nxt, length2 + 1):
                            _sum2 = sum(c2)
                            if _sum1 == _sum2:
                                tag = False
                                break
                        if not tag:
                            break
                    if not tag:
                        break
                if not tag:
                    break
        if tag:
            result += sum(array)
        line = response.readline()
    return result


if __name__ == "__main__":
    print solve()
