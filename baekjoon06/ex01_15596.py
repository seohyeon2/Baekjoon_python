# 15596번 : 정수 n개의 합

# 1번 풀이 : 내장함수 이용
'''
def solve(a):
    ans = sum(a)
    return ans
'''

# 2번 풀이 : 반복문 이용
def solve(a):
    ans = 0
    for i in a:
        ans += i
    return ans