'''
title     : Find a string
subdomain : Strings
domain    : Python
author    : Sohayel Mahmud
created   : 26 Nov, 2025
'''

def count_substring(string, sub_string):
    sum = 0
    for i in range(len(string) - len(sub_string) + 1):
        if string[i : i + len(sub_string)] == sub_string:
            sum +=1
    return sum

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)