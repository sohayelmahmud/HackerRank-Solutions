'''
title     : Polar Coordinates
subdomain : Math
domain    : Python
author    : Sohayel Mahmud
created   : 26 Nov, 2025
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT

import cmath

z = complex(input())
p = cmath.polar(z)

print(p[0])
print(p[1])