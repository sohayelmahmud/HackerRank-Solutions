'''
title     : Set .add()
subdomain : Sets
domain    : Python
author    : Sohayel Mahmud
created   : 26 Nov, 2025
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == "__main__":
    country = set()
    n = int(input())

    for i in range(n):
        stamp = input().strip()
        country.add(stamp)
    print(len(country))