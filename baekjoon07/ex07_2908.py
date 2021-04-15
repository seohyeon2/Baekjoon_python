# 2908번 : 상수

# 1번 풀이
'''
a,b = input().split()

a = int(a[::-1])
b = int(b[::-1])

if (a > b) :
    print(a)
else :
    print(b)
'''

# 2번 풀이
print(max(input()[::-1].split()))