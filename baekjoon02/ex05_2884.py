# 2884번 : 알람시계

h,m = map(int, input().split())

if m > 44 : print(h,m-45)
elif h > 0 and m < 45 : print(h-1,m+15)
else : print(23,m+15)