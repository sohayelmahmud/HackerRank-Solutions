'''
title     : Set .discard(), .remove() &amp; .pop()
subdomain : Sets
domain    : Python
author    : Sohayel Mahmud
created   : 26 Nov, 2025
'''

if __name__ == "__main__":
    n = int(input())
    s = set(map(int, input().split()))
    num_cmd = int(input())

    for i in range(num_cmd):
        cmd = list(input().strip().split())

        if cmd[0] == 'pop':
            s.pop()
        elif cmd[0] == 'remove':
            s.remove(int(cmd[1]))
        else:
            s.discard(int(cmd[1]))

    print(sum(s))