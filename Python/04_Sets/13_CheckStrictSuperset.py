'''
title     : Check Strict Superset
subdomain : Sets
domain    : Python
author    : Sohayel Mahmud
created   : 26 Nov, 2025
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == "__main__":
    a = set(map(int, input().strip().split()))
    n = int(input())
    superset = True

    for i in range(n):
        b = set(map(int, input().strip().split()))
        if not a.issuperset(b):
            superset = False

    print(superset)
