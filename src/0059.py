# -*- coding: utf-8 -*-
# !/bin/env python2

from itertools import permutations
import urllib2


def solve():
    response = urllib2.urlopen(
        "https://projecteuler.net/project/resources/p059_cipher.txt"
    )
    l = map(int, response.read().split(","))
    print "fetch done"
    alpha_list = [i for i in range(ord('a'), ord('z') + 1)]
    for keys in permutations(alpha_list, 3):
        _l = l[:]
        for i in range(len(l)):
            _l[i] = _l[i] ^ keys[i % 3]
        _s, tag = "".join(map(chr, _l)), True
        for ch in _s:
            if (
                not ch.isalpha() and
                not ch.isdigit() and
                ch not in [" ", ",", ".", "!", "?", ";",
                           "(", ")", "\"", "\'", "\n", "\r"]
            ):
                tag = False
                break
        if tag:
            print _s
            print reduce(lambda x, y: x + y, _l)
            break


if __name__ == "__main__":
    solve()
