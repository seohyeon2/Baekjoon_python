# 1316번 : 그룹 단어 체커

# 1번 풀이
'''
a = int(input())
result = 0
for i in range(a):
    word = input()
    alphabet = [0]*26
    
    value = 1
    last = word[0]
    for j in word:
        if last == j and alphabet[ord(j)-97] == 0:
            alphabet[ord(j)-97] = 1
        elif last != j and alphabet[ord(j)-97] != 0:
            value = 0
            break
        elif last != j and alphabet[ord(j)-97] == 0:
            alphabet[ord(j)-97] = 1
            last = j
 
    result += value
print(result, end="")
'''

# 2번 풀이
n = int(input())

for _ in range(n):
    word = input()
    for i in range(1,len(word)):
        if(word.find(word[i-1]) > word.find(word[i])):
            n -= 1
            break
print(n)