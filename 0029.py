# -*- coding: utf-8 -*-

_list = []
for a in range(2, 101):
    for b in range(2, 101):
        _list.append(a ** b)
_list = set(_list)
print len(_list)
