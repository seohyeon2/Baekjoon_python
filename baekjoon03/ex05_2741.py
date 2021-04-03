# 2741번 : N 찍기

# 1번 풀이
'''
n = int(input())

for i in range(1,n+1):
    print(i)
'''

# 2번 풀이 : comprehension 표현식
n = int(input())
[print(i+1) for i in range(n)]

#comprehension 표현식 : [출력 표현식 for iterable자료 요소 in iterable 자료형]