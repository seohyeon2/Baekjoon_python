# 2742번 : 기찍 N

# 1번 풀이
'''
n = int(input())

for i in range(n,0,-1):      # range(초기값(포함),종료값(미포함),증감) 
    print(i)
'''

# 2번 풀이
n = int(input())

for i in reversed(range(n)):
    print(i+1)