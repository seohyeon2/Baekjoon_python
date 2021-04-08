# 1065번 : 함수

# 1번 풀이 : for문 이용
def hansu(n) :
    if n < 100 :
        return n
    else:  
        cnt = 99
        for i in range(100,n+1):
            nums = list(map(int,str(i)))
            if (nums[0] - nums[1]) == (nums[1] - nums[2]) :
                cnt += 1
    return cnt

n = int(input())
print(hansu(n))