'''
title     : sWAP cASE
subdomain : Strings
domain    : Python
author    : Sohayel Mahmud
created   : 26 Nov, 2025
'''

def swap_case(s):
    updated_s = ""
    for c in s:
        if c.isupper():
            updated_s += c.lower()
        elif c.islower():
            updated_s += c.upper()
        else:
            updated_s += c
    return updated_s

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)