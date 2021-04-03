# 8393번 : 합

sum = 0
n = int(input())

for i in range(n+1):     # 범위 : 1 ~ n  /  원래 범위 : 0 ~ n-1  
    sum += i             # 초기화 안하면 오류!

print(sum)