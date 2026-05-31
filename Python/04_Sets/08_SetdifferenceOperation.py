'''
title     : Set .difference() Operation
subdomain : Sets
domain    : Python
author    : Sohayel Mahmud
created   : 26 Nov, 2025
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == "__main__":
    n = int(input())
    english = set(map(int, input().strip().split()))
    m = int(input())
    french = set(map(int, input().strip().split()))

    print(len(english.difference(french)))