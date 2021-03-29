# 2588번 : 곱셈

# 1번째 풀이
'''
a = int(input())
b = int(input())

print(a*(b%100%10))
print(a*(b%100//10))
print(a*(b//100))
print(a*b)
'''

# 2번째 풀이
a = int(input())
b = input()
for i in b[::-1] :
    print(a * int(i))
print(a*int(b))