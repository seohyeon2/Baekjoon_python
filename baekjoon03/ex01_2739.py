# 2739번 : 구구단

# 1번 풀이
'''
n = int(input())
for i in range(1,10):
    print(n, "*", i, "=", n*i)
'''

# 2번 풀이
n = int(input())
for i in range(1,10):
    print("%d * %d = %d" %(n,i,n*i))