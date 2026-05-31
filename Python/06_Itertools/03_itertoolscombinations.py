'''
title     : itertools.combinations()
subdomain : Itertools
domain    : Python
author    : Sohayel Mahmud
created   : 26 Nov, 2025
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT

import itertools

s,n = list(map(str, input().split(' ')))
n = int(n) +1
s = sorted(s)

for i in range(1, n):
    for j in itertools.combinations(s, i):
        print(''.join(j))