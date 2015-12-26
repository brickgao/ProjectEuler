# -*- coding: utf-8 -*-


def is_pentagon(_num):
    _num = _num * 24 + 1
    if int(float(_num) ** 0.5) ** 2 != _num:
        return False
    _num = int(float(_num) ** 0.5) + 1
    if _num % 6:
        return False
    else:
        return True


def is_triangle(_num):
    _num = 1 + 8 * _num
    if int(float(_num) ** 0.5) ** 2 != _num:
        return False
    _num1 = - 1 - int(float(_num) ** 0.5)
    _num2 = - 1 + int(float(_num) ** 0.5)
    if (_num1 % 2 == 0 and _num1 > 0) or (_num2 % 2 == 0 and _num2 > 0):
        return True
    else:
        return False


_n = 144
while True:
    _num = _n * (2 * _n - 1)
    if is_pentagon(_num) and is_triangle(_num):
        print _num
        break
    _n += 1
