# -*- coding: utf-8 -*-


_is = [True for x in range(10 ** 6 + 1)]
_is[0], _is[1] = False, False
_p = [2]
_e = int((10 ** 6 + 1) ** 0.5) + 1
for i in range(4, 10 ** 6 + 1, 2):
    _is[i] = False
for i in range(3, _e, 2):
    if _is[i]:
        for j in range(i ** 2, 10 ** 6, i * 2):
            _is[j] = False
for i in range(3, 10 ** 6 + 1, 2):
    if _is[i]:
        _p.append(i)

for _e in _p:
    _flag = False
    _s = str(_e)
    _len = (1 << len(_s)) - 1
    for _i in range(1, _len):
        _min = 0xfffffff
        _c = bin(_i)[2:]
        _cnt = 0
        for _j in range(10):
            if _c[0] == '1' and _j == 0:
                continue
            _tmp = _s
            for _k in range(len(_c)):
                if _c[_k] == '1':
                    _tmp = _tmp[:_k] + str(_j) + _tmp[_k + 1:]
            if _is[int(_tmp)]:
                _min = min(_min, int(_tmp))
                _cnt += 1
        if _cnt == 8:
            _flag = True
            print _min
            break
    if _flag:
        break
