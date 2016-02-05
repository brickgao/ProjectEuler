# !/bin/env python2
# -*- coding: utf-8 -*-


def solve():
    # https://oeis.org/A102341
    limit, result = 10 ** 9, 0
    side, _side, length, tag = 1, 1, 0, 1
    while length < limit:
        side, _side, tag = _side, 4 * _side - side + 2 * tag, -tag
        result += length
        length = 3 * _side - tag
    return result


if __name__ == "__main__":
    print solve()
