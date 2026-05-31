'''
title     : Iterables and Iterators
subdomain : Itertools
domain    : Python
author    : Sohayel Mahmud
created   : 26 Nov, 2025
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import combinations

n = int(input())
ar = input().split()
k = int(input())
comb_list = list(combinations(ar, k))
a_list = [e for e in comb_list if "a" in e]
print(len(a_list) / len(comb_list))