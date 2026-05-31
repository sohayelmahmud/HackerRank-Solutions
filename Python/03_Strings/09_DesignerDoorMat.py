'''
title     : Designer Door Mat
subdomain : Strings
domain    : Python
author    : Sohayel Mahmud
created   : 26 Nov, 2025
'''

N, M = map(int, input().split())
for i in range(1, N, 2):
    print(int((M - 3 * i) / 2) * "-" + (i * ".|.") + int((M - 3 * i) / 2) * "-")
print(int((M - 7) / 2) * "-" + "WELCOME" + int((M - 7) / 2) * "-")
for i in range(N - 2, -1, -2):
    print(int((M - 3 * i) / 2) * "-" + (i * ".|.") + int((M - 3 * i) / 2) * "-")