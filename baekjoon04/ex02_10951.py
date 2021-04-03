# 10951번 : A+B - 4

# 1번풀이
'''
while 1 : 
    try:
        a,b = map(int,input().split())
        print(a+b)
    except: 
        break
'''

# 2번
import sys

for i in sys.stdin:            #표준 입력만 가능
    a, b = map(int, i.split())
    print(a+b)