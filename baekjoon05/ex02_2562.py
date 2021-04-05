# 2562번 : 최댓값

# 1번 풀이 : 내장함수 이용
'''
nums = []
for i in range(9):
    nums.append(int(input()))
print(max(nums),nums.index(max(nums))+1)
'''

# 2번 풀이 : 반복문, 조건문 이용
import sys

n_max = 0
n_index = 0

for i in range(9):
    n = int(sys.stdin.readline())
    if n > n_max : 
        n_max = n
        n_index = i+1
print(n_max,n_index)
    