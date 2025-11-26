'''
title     : Tuples
subdomain : Basic Data Types
domain    : Python
author    : Sohayel Mahmud
created   : 26 Nov, 2025
'''

if __name__ == "__main__":
    n = int(input())
    integer_list = map(int, input().split())
    t = tuple(integer_list)
    print(hash(t))