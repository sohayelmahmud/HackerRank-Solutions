'''
title     : Symmetric Difference
subdomain : Sets
domain    : Python
author    : Sohayel Mahmud
created   : 26 Nov, 2025
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == "__main__":
    m = int(input())
    a = set(map(int, input().strip().split()))
    n = int(input())
    b = set(map(int, input().strip().split()))

    p = sorted(a.symmetric_difference(b))

    for i in p:
        print(i)