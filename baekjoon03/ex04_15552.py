# 15552번 : 빠른 A+B

import sys
t = int(sys.stdin.readline())

for _ in range(t):
    a,b = map(int,sys.stdin.readline().split())
    print(a+b)

# strip()  : ()안이 공백일 경우, whitespace(띄어쓰기(''), 탭(\t), 엔터(\n))을 제거해주는 함수
# rstrip() : ()안이 공백일 경우, 오른쪽의 whitespace를 삭제해주는 함수
# split()  : 어떤 문자를 기반으로 나누는 함수, ()안이 공백일 시 띄어쓰기, 탭으로 나누어짐