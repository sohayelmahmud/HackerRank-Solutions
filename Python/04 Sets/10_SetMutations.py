'''
title     : Set Mutations
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

    for i in range(n):
        cmd = list(input().strip().split())
        b = set(map(int, input().strip().split()))

        if cmd[0] == 'intersection_update':
            a.intersection_update(b)
        elif cmd[0] == 'update':
            a.update(b)
        elif cmd[0] == 'symmetric_difference_update':
            a.symmetric_difference_update(b)
        else:
            a.difference_update(b)

    print(sum(a))