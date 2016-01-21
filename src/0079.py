# -*- coding: utf-8 -*-
# !/bin/env python2

import urllib
from collections import defaultdict


def solve():
    mp, in_vals = defaultdict(lambda: []), defaultdict(lambda: 0)
    data = urllib.urlopen(
        "https://projecteuler.net/project/resources/p079_keylog.txt"
    ).read().split("\n")[:-1]
    for passcode in data:
        passcode_list = map(int, passcode)
        mp[passcode_list[0]].append(passcode_list[1])
        mp[passcode_list[1]].append(passcode_list[2])
        in_vals[passcode_list[0]] += 0
        in_vals[passcode_list[1]] += 1
        in_vals[passcode_list[2]] += 1
    vis, result = set(), ""
    while True:
        tag, minn = True, 10000
        for key in in_vals.keys():
            if key not in vis and in_vals[key] == 0:
                if key < minn:
                    minn, tag = key, False
        if tag:
            break
        result += str(minn)
        vis.add(minn)
        for nxt in mp[minn]:
            in_vals[nxt] -= 1
    return result


if __name__ == "__main__":
    print solve()
