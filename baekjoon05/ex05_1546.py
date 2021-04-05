# 1546번 : 평균

# 1번 풀이 : 내장 함수 이용
'''
n = int(input())
origin_score = list(map(int,input().split()))
max_score = max(origin_score)

new_score = []

for score in origin_score:
    new_score.append(score/max_score*100)

print(sum(new_score)/n)
'''

# 2번 풀이 : 반복문, 조건문 이용
n = int(input())
score = list(map(int,input().split()))
score_max = 0
sum = 0

for i in range(n):
    if score_max < score[i]:
        score_max = score[i]

for j in range(n):
    score[j] = score[j] / score_max * 100
    sum += score[j]

print(sum/n)