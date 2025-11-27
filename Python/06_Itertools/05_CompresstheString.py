'''
title     : Compress the String!
subdomain : Itertools
domain    : Python
author    : Sohayel Mahmud
created   : 26 Nov, 2025
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT

import itertools

s = input().strip()
group = []
key = []
for k, g in itertools.groupby(s):
    group.append(list(g))
    key.append(k)
for i in range(len(group)):
    group_length = len(group[i])
    k = int(key[i])
    print((group_length, k), end=" ")