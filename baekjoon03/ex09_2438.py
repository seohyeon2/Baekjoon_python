# 2438번 : 별찍기 - 1

# 1번 풀이
'''
n = int(input())

for i in range(1,n+1):
    for j in range(i):
        print("*",end="")
    print()
'''

# 2번 풀이
'''
n = int(input())

for i in range(1,n+1):
    print("*" * i)
'''

# 3번 풀이
[print("*" * i) for i in range(1,int(input())+1)]