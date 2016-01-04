# -*- coding: utf-8 -*-
# !/bin/env python2

vis, tmp, result = set(), [], []


def solve():
    rec = [dict() for i in range(6)]
    func_dict = {
        0: lambda n: n * (n + 1) / 2,
        1: lambda n: n * n,
        2: lambda n: n * (3 * n - 1) / 2,
        3: lambda n: n * (2 * n - 1),
        4: lambda n: n * (5 * n - 3) / 2,
        5: lambda n: n * (3 * n - 2)
    }
    for i in range(6):
        cnt = 1
        while True:
            num = func_dict[i](cnt)
            s_num = str(num)
            if len(s_num) >= 5:
                break
            if len(s_num) == 4:
                pre_digitals = s_num[:2]
                if pre_digitals not in rec[i]:
                    rec[i][pre_digitals] = []
                rec[i][pre_digitals].append(num)
            cnt += 1

    def dfs(pre_digitals, now, lefts):
        global vis, tmp, result
        if len(tmp) == 6:
            if pre_digitals == str(tmp[0])[:2]:
                result = tmp[:]
        else:
            if result or pre_digitals not in rec[now]:
                return
            for num in rec[now][pre_digitals]:
                if (now, num) not in vis:
                    tmp.append(num)
                    vis.add((now, num))
                    for nxt in lefts:
                        dfs(str(num)[2:], nxt, lefts - {nxt})
                    vis.remove((now, num))
                    tmp.pop()

    global vis, tmp, result
    lefts = set([1, 2, 3, 4, 5])
    for pre_digitals in rec[0]:
        for num in rec[0][pre_digitals]:
            tmp.append(num)
            vis.add((0, num))
            for nxt in lefts:
                dfs(str(num)[2:], nxt, lefts)
            vis.remove((0, num))
            tmp.pop()
    print result, sum(result)


if __name__ == "__main__":
    solve()
