# -*- coding: utf-8 -*-

vis = [0 for x in range(4 * 10 ** 6)]
ret1, ret2 = 0, 0
for i in range(2, 10 ** 6):
    if vis[i]:      continue
    if not i % 2:   _ = i / 2
    else:           _ = 3 * i + 1
    _r = [i, _]
    tag = True
    while _ != 1:
        if not _ % 2:   _ /= 2
        else:           _ = 3 * _ + 1
        if _ < 10 ** 6 and vis[_]:
            _t = len(_r) + vis[_]
            for j in range(len(_r)):
                if _r[j] < 10 ** 6:
                    vis[_r[j]] = _t - j
            tag = False
            break
        _r.append(_)
    if tag:
        _t = len(_r)
        for j in range(_t):
            if _r[j] < 10 ** 6:
                vis[_r[j]] = _t - j
    if ret1 < _t:   ret1, ret2 = _t, i
print ret2
        
