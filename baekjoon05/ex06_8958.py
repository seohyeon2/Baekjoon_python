# 8958번 : OX퀴즈
t = int(input())
for _ in range(t):
    input_ox = list(input())
    score = 0
    cnt = 0
    for ox in input_ox:
        if ox == 'O':
            cnt += 1
            score += cnt
        elif ox == 'X':
            score += 0
            cnt = 0
    print(score)