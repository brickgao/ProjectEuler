#!/bin/env python3
# -*- coding: utf-8 -*-


def solve():
    num, cnt = 1, 0
    while float(cnt) / float(num) < 0.99:
        num += 1
        flags = [0, 0]
        last, _num = num % 10, num // 10
        while _num > 0:
            now, _num = _num % 10, _num // 10
            if now > last:
                flags[0] = 1
            elif now < last:
                flags[1] = 1
            last = now
        if flags[0] * flags[1] > 0:
            cnt += 1
    return num


if __name__ == "__main__":
    print(solve())
