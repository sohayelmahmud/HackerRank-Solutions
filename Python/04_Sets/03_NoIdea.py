'''
title     : No Idea!
subdomain : Sets
domain    : Python
author    : Sohayel Mahmud
created   : 26 Nov, 2025
'''


#!/usr/bin/env python3

if __name__ == "__main__":
    happiness = 0
    n, m = map(int, input().strip().split(' '))
    arr = list(map(int, input().strip().split(' ')))

    like = set(map(int, input().strip().split(' ')))
    dislike = set(map(int, input().strip().split(' ')))

    for i in arr:
        if i in like:
            happiness += 1
        elif i in dislike:
            happiness -= 1

    print(happiness)