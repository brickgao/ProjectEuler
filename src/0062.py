# -*- coding: utf-8 -*-
# !/bin/env python2

from collections import defaultdict
import math


def solve():
    i, digitals2num = 0, defaultdict(lambda: [])
    while True:
        num_pow3 = int(math.pow(i, 3))
        digitals = tuple(sorted(str(num_pow3)))
        digitals2num[digitals].append(num_pow3)
        if len(digitals2num[digitals]) >= 5:
            print digitals2num[digitals], min(digitals2num[digitals])
            break
        i += 1


if __name__ == "__main__":
    solve()
