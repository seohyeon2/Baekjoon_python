# 11022번 : A+B - 8

# 1번 풀이
'''
import sys
t = int(sys.stdin.readline())

for i in range(t):
    a,b = map(int,sys.stdin.readline().split())
    c = a+b
    print("Case #%d: %d + %d = %d" %(i+1,a,b,c))
'''

# 2번 풀이 : f-string 작성법
t = int(input())

for i in range(1,t+1):
    a,b = map(int,input().split())
    print(f'Case #{i}: {a} + {b} = {a+b}')