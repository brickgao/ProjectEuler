# -*- coding: utf-8 -*-
# !/bin/env python2


def solve():
    result = 1
    for num in range(2, 10):
        power = 1
        while True:
            powed_num = num ** power
            if len(str(powed_num)) == power:
                result += 1
            else:
                break
            power += 1
    return result


if __name__ == "__main__":
    print solve()
