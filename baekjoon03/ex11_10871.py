# 10871번 : X보다 작은 수

# 1번 풀이
'''
n,x = map(int,input().split())
a = list(map(int,input().split()))
for i in range (n):
    if a[i] < x :
        print(a[i],end=" ")
'''

# 2번 풀이
n,x = map(int,input().split())
a = map(int,input().split(maxsplit=n))    # 수열 a 값을 n개까지만 받음
for i in a:
    if i < x :
        print(i,end=" ")