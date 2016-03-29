#!/bin/env python3
# -*- coding: utf-8 -*-


def solve():
    limit = 2000
    result, mp, n = 0, [], limit * limit
    for k in range(1, n + 1):
        if k <= 55:
            mp.append(
                (100003 - 200003 * k + 300007 * k ** 3) % 1000000 - 500000
            )
        else:
            mp.append(
                (mp[k - 25] + mp[k - 56] + 1000000) % 1000000 - 500000
            )
    for y in range(limit):
        _sum = 0
        for x in range(limit):
            _sum = max(0, _sum + mp[x + y * limit])
            result = result if result > _sum else _sum
    for x in range(limit):
        _sum = 0
        for y in range(limit):
            _sum = max(0, _sum + mp[x + y * limit])
            result = result if result > _sum else _sum
    for x in range(limit):
        for diff_x, diff_y in [(1, 1), (-1, 1)]:
            _sum, _x, _y = 0, x, 0
            while 0 <= _x < limit and 0 <= _y < limit:
                _sum = max(0, _sum + mp[_x + _y * limit])
                _x, _y = _x + diff_x, _y + diff_y
                result = result if result > _sum else _sum
    for y in range(limit):
        for _x, diff_x, diff_y in [(0, 1, 1), (limit - 1, -1, 1)]:
            _sum, _y = 0, y
            while 0 <= _x < limit and 0 <= _y < limit:
                _sum = max(0, _sum + mp[_x + _y * limit])
                _x, _y = _x + diff_x, _y + diff_y
                result = result if result > _sum else _sum
    return result


if __name__ == "__main__":
    print(solve())
