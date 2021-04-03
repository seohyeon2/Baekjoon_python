# 10950번 : A+B - 3

t = int(input())
for _ in range(t) :
    a,b = map(int,input().split())
    print(a+b)

# 숫자 요소를 변수로 선언한여 사용할 필요가 없을 때 _ 표현 가능
# range 함수에서 괄호안에 숫자가 1개인 경우 시작값은 0, 끝값은 t-1