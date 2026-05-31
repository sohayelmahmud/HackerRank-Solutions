'''
title     : Check Subset
subdomain : Sets
domain    : Python
author    : Sohayel Mahmud
created   : 26 Nov, 2025
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == "__main__":
    t = int(input())

    for i in range(t):
        n = int(input())
        a = set(map(int, input().strip().split()))
        m = int(input())
        b = set(map(int, input().strip().split()))

        if a.issubset(b):
            print(True)
        else:
            print(False)