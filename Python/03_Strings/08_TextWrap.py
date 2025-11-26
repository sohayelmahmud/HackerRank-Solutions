'''
title     : Text Wrap
subdomain : Strings
domain    : Python
author    : Sohayel Mahmud
created   : 26 Nov, 2025
'''

import textwrap

def wrap(string, max_width):
    return textwrap.fill(string, max_width)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)