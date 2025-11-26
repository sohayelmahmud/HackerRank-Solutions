'''
title     : The Captains Room
subdomain : Sets
domain    : Python
author    : Sohayel Mahmud
created   : 26 Nov, 2025
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == "__main__":
    k = int(input())
    LIST = list(map(int, input().strip().split()))
    SET = set(LIST)

    print(((sum(SET)*k) - (sum(LIST)))//(k-1))