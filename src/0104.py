# !/bin/env python2
# -*- coding: utf-8 -*-

from decimal import Decimal, Context


def solve():
    mod, cnt, num1, num2 = 10 ** 9, 2, 1, 1
    x, y = (
        Decimal(1) / Decimal(5).sqrt(),
        (Decimal(1) + Decimal(5).sqrt()) / Decimal(2)
    )
    _context = Context()
    while True:
        num1, num2 = num2, (num1 + num2) % mod
        _set = set(str(num1))
        if '0' not in _set and len(_set) == 9:
            _tmp = x.log10() + cnt * y.log10()
            _num = int(_context.power(10, _tmp - int(_tmp) + 8))
            _set = set(str(_num))
            if '0' not in _set and len(_set) == 9:
                return cnt
        cnt += 1


if __name__ == "__main__":
    print solve()
