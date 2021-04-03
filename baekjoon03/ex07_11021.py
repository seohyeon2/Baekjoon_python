# 11021번 : A+B - 7

# 1번 풀이
'''
import sys
t = int(sys.stdin.readline())

for i in range(t):
    a,b = map(int,sys.stdin.readline().split())
    print("Case #%d: %d" %(i+1,a+b))
'''

# 2번 풀이
t = int(input())

for i in range(1,t+1):
    a,b = map(int,input().split())
    print("Case #"+str(i)+":",a+b)