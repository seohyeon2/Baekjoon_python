# 4344번 : 평균은 넘겠지
c = int(input())

for i in range(c):
    cnt = 0
    score = list(map(int,input().split()))
    avg = sum(score[1:]) // score[0]

    for j in score[1:]:
        if avg < j:
            cnt += 1
    print("%.3f%%"%((cnt/score[0]) * 100))