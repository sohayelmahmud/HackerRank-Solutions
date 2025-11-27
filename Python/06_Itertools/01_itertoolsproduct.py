'''
title     : itertools.product()
subdomain : Itertools
domain    : Python
author    : Sohayel Mahmud
created   : 26 Nov, 2025
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT

import itertools

a,b = list(map(int, input().split())), list(map(int, input().split()))

cross = list(itertools.product(a,b))

for i in cross:
    print(i, end=' ')