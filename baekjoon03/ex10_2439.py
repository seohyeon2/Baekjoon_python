# 2439번 : 별찍기 - 2

# 1번 풀이
'''
n = int(input())

for i in range(1,n+1):
    print(" " * (n-i), end="")
    print("*" * i)
'''

# 2번 풀이
n = int(input())

for i in range(1,n+1):
    print(" " * (n-i) + "*" * i)