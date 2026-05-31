'''
title     : Find Angle MBC
subdomain : Math
domain    : Python
author    : Sohayel Mahmud
created   : 26 Nov, 2025
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT

import math

ab = float(input())
bc = float(input())

theta_rad = math.atan(ab / bc)
theta_deg = int(round(math.degrees(theta_rad)))

print(f"{theta_deg}\u00B0") # '\u00B0' is the Unicode for the degree symbol
