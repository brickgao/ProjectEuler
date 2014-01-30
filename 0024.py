# -*- coding: utf-8 -*-

import itertools

_arr = []
for _ in itertools.permutations('0123456789', 10):
    _arr.append(_)
_len = len(_arr)
_now = 10 ** 6 - 1
_ret = ''
for i in _arr[_now]:
    _ret += i
print _ret
