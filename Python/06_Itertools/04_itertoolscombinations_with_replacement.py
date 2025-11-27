'''
title     : itertools.combinations_with_replacement()
subdomain : Itertools
domain    : Python
author    : Sohayel Mahmud
created   : 26 Nov, 2025
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import *

s, n = input().split()
n = int(n)
s = sorted(s)
for i in combinations_with_replacement(s, n):
    print("".join(i))