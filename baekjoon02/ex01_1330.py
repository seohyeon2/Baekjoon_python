# 1330번 : 두 수 비교하기

# 1번 풀이
'''
a,b = map(int,input().split())
if a>b : print(">")
elif a<b : print("<")
else : print("==")
'''

# 2번 풀이
a,b = map(int,input().split())
print('>' if a>b else '<' if a<b else '==')

# 삼항연산자 : (참일때 값) if (조건식) else (거짓일 때 값)
# 중첩 삼항 표현식 : (참일때 값) if (조건식) else [ (참일때 값) if (조건식) else (거짓일 때 값)]
#                    [ ]는 편의를 위해 추가함 