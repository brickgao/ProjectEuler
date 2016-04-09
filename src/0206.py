#!/bin/env python3
# -*- coding: utf-8 -*-

import math


def solve():
    template = "1{}2{}3{}4{}5{}6{}7{}8{}900"
    upper_bound = int(math.sqrt(int(template.format(*([9] * 9)))) / 10) + 2
    lower_bound = int(math.sqrt(int(template.format(*([0] * 9)))) / 10)
    num = lower_bound = int(str(lower_bound)[:-1] + "3")
    steps = [4, 6]
    while num < upper_bound:
        for step in steps:
            now = str(num * num)
            if all(now[i] == str(i // 2 + 1) for i in range(0, 17, 2)):
                return num * 10
            num += step


if __name__ == "__main__":
    print(solve())
