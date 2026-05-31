'''
title     : Print Function
subdomain : Introduction
domain    : Python
author    : Sohayel Mahmud
created   : 26 Nov, 2025
'''

from __future__ import print_function

if __name__ == '__main__':
    n = int(input())
    for i in range(1, n+1):
        print(i, sep='', end='')
