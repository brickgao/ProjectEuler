# -*- coding:utf8 -*-


def num2words(n):
    ones = ["", "one", "two", "three", "four", "five",
            "six", "seven", "eight", "nine"]
    tens = ["ten", "eleven", "twelve", "thirteen", "fourteen",
            "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    twenties = ["","", "twenty", "thirty", "forty",
                "fifty", "sixty", "seventy", "eighty", "ninety"]
    if n < 10:      return ones[n]
    if n < 20:      return tens[n - 10]
    if n < 100:     return twenties[n / 10] + ' ' + ones[n % 10]
    if n < 1000:
        if not n % 100:
            return ones[n / 100] + ' hundred'
        elif (n % 100) < 10:
            return ones[n / 100] + ' hundred and ' + ones[n % 100]
        elif (n % 100) < 20:
            return ones[n / 100] + ' hundred and ' + tens[n % 100 - 10]
        else:
            return ones[n / 100] + ' hundred and ' + twenties[(n % 100) / 10] + ' ' + ones[n % 10]
    if n == 1000:   return 'one thousand'

ret = 0
for i in range(1, 1001):
    _s = num2words(i)
    for _ in _s:
        if _ != ' ':
            ret += 1
print ret
