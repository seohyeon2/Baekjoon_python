# 2577번 : 숫자의 개수

# 1번 풀이 : 내장 함수 이용
'''
a = int(input())
b = int(input())
c = int(input())

multi = str(a * b * c)
for i in range(10):
    print(multi.count(str(i)))
'''

# 2번 풀이 : 반복문, 조건문 이용
a = int(input())
b = int(input())
c = int(input())

multi = str(a * b * c)

for i in range(10):
    cnt = 0
    for j in range(len(multi)):
        if i == int(multi[j]):
         cnt += 1
    print(cnt)