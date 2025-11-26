'''
title     : Write a function
subdomain : Introduction
domain    : Python
author    : Sohayel Mahmud
created   : 26 Nov, 2025
'''

def is_leap(year):
    leap = False

    if year % 4 == 0:
        leap = True
        if year % 100 == 0:
            if year % 400 == 0:
                leap = True
            else:
                leap = False
    else:
        leap = False

    return leap
