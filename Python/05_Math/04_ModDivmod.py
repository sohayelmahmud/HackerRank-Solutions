'''
title     : Mod Divmod
subdomain : Math
domain    : Python
author    : Sohayel Mahmud
created   : 26 Nov, 2025
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT

a,b = int(input()), int(input())
d = divmod(a,b)

# d= divmod(int(input()), int(input())) #more simplified

print(d[0])
print(d[1])
print(d)