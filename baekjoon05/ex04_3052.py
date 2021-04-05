# 3052번 : 나머지

# 1번 풀이 : set() 이용
'''
import sys
nums = []
for i in range(10):
    n = int(input())
    nums.append(n % 42)
print(len(set(nums)))
'''

# 2번 풀이 : 반복문, 조건문 이용
import sys
nums = []
cnt = []

for i in range(10):
    n = int(input())
    nums.append(n % 42)

for j in range(len(nums)):
    if nums[j] not in cnt:
        cnt.append(nums[j])

print(len(cnt))