'''
title     : Triangle Quest 2
subdomain : Math
domain    : Python
author    : Sohayel Mahmud
created   : 26 Nov, 2025
'''



for i in range(1,int(input())+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print(((10**i - 1)//9)**2)