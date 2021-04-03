# 1110번 : 더하기 싸이클

n = int(input())
origin = n
cnt = 0
temp1 = 0 
temp2 = 0

while (True) : 
    temp1 = (n // 10) + (n % 10)
    temp2 = (n % 10)*10 + (temp1 % 10)
    cnt += 1 
    n = temp2
    if temp2 == origin :
        print(cnt)
        break