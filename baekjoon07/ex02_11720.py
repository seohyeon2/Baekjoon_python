# 11720번 : 숫자의 합

# 1번 풀이 : for문 이용
'''
n = int(input())
li = list(input())
result = 0
for i in li :
    result += int(i)
print(result)
'''

# 2번 풀이 : sum함수 이용
n = input()
print(sum(map(int,input())))