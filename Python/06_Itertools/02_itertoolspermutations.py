'''
title     : itertools.permutations()
subdomain : Itertools
domain    : Python
author    : Sohayel Mahmud
created   : 26 Nov, 2025
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT

import itertools

a,b = list(map(str, input().split(' ')))
a = sorted(a)
perm = list(itertools.permutations(a,int(b)))
for i in perm:
    print(''.join(i))