# -*- coding: utf-8 -*-
# __author__ = 'Herixth'

import decimal
decimal.getcontext().prec = 50


def main():
    n = int(input('input n:'))
    s = decimal.Decimal((3**0.5) * 1.5)
    inc = 6
    x = 1
    h = float()
    while inc <= n / 2:
        h = (1 - (x / 2)**2)**0.5
        s = s + inc * x * (1 - h) / 2
        x = ((x / 2)**2 + (1 - h)**2)**0.5
        inc *= 2
    print("%.50lf" % s)


if __name__ == '__main__':
    main()
