# Enter your code here. Read input from STDIN. Print output to STDOUT
t = int(input())

for _ in range(t):
    s = input().strip()

    even = s[::2]
    odd = s[1::2]

    print(even, odd)