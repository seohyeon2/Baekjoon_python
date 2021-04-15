# 10809번 : 알파벳 찾기

# 1번 풀이 : chr 함수 이용
'''
s = input()
a = list(range(97,123))
for i in a:
    print(s.find(chr(i)))
'''

# 2번 풀이 : 아스키코드 이용
'''
S = input()
check = [-1]*26
 
for i in range(len(S)):
    if check[ord(S[i])-97] != -1:
        continue
    else:
        check[ord(S[i])-97] = i
        
for i in range(26):
    print(check[i], end=' ')
'''

# 4번 풀이 : string 이용
'''
import string
a = input()
for i in string.ascii_lowercase:
    print(a.find(i), end=" ")
'''    

# 4번 풀이 : index 이용
import string
s = input()
a = string.ascii_lowercase
for i in range(0,len(a)):
    if a[i] in s:
        print(s.index(a[i]), end = " ")
    else:
        print(-1, end = " ")