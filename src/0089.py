# !/bin/env python2
# -*- coding: utf-8 -*-

import re
import urllib


def solve():
    response = urllib.urlopen(
        "https://projecteuler.net/project/resources/p089_roman.txt"
    )
    data = response.read()
    return len(data) - len(re.sub("DCCCC|LXXXX|VIIII|CCCC|XXXX|IIII",
                                  "  ", data))


if __name__ == "__main__":
    print solve()
