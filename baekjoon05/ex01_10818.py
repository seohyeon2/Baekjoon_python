# 10818번 : 최소, 최대

# 1번 풀이 : 내장함수 이용
'''
n = int(input())
arr = list(map(int,input().split()))
print('{} {}'.format(min(arr),max(arr)))
'''

# 2번 풀이 : 반복문 이용
'''
n = int(input())
arr = list(map(int,input().split()))
max = arr[0]
min = arr[0]
for i in arr:
    if i > max:
        max = i
    if i < min:
        min = i
print(min,max)
'''

# 3번 풀이 : sort 이용
n = int(input())
arr = list(map(int,input().split()))
arr.sort()
print(arr[0],arr[n-1])