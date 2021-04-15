# 5622번 : 다이얼

# 1번 풀이
'''
dial = input()
time = 0

for d in dial:
    if d in ['A', 'B', 'C']:
        time += 3
    elif d in ['D','E', 'F']:
        time += 4
    elif d in ['G', 'H', 'I']:
        time += 5
    elif d in ['J', 'K', 'L']:
        time += 6
    elif d in ['M', 'N', 'O']:
        time += 7
    elif d in ['P', 'Q', 'R', 'S']:
        time += 8
    elif d in ['T', 'U', 'V']:
        time += 9
    elif d in ['W', 'X', 'Y', 'Z']:
        time += 10
    else:
        time += 11

print(time)
'''

# 2번 풀이
'''
time = 0
alpabet = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
s = input()

for i in range(len(s)):
    for j in alpabet:
        if s[i] in j:
            time += alpabet.index(j)+3
print(time)
'''
# 3번 풀이
print(sum(min(ord(c)-64,25)*28//89+3 for c in input()))