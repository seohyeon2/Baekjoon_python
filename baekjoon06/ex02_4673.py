# 4673번 : 셀프 넘버

# 1번 풀이 : for문 사용
'''
def d(n):
    add_number = n
    for i in list(str(n)):
        add_number += int(i)
    return add_number

have_ctor = []
for i in range(1,10001):
    a = d(i)
    have_ctor.append(a)

for no_ctor in range(1,10001):
    if no_ctor in have_ctor: 
        pass
    else:
        print(no_ctor)
'''

# 2번 풀이 : sum함수 사용
'''
def d(n):
    n += sum(map(int,str(n)))
    return n

have_ctor = [0]*10001

for i in range(1,10001):
    have_ctor[i] = d(i)

for no_ctor in range(1,10001):
    if no_ctor not in have_ctor:
        print(no_ctor)
'''

# 3번 풀이 : while문 사용
def d(n):
    result = n
    while n != 0:
        result += n%10
        n //= 10
    return result

have_ctor = []
no_ctor = list(range(1,10001))

for i in list(range(1,10001)):
    have_ctor.append(d(i))

for j in range(10000):
    a = have_ctor[j]
    if a in no_ctor:
        no_ctor.remove(a)

for k in no_ctor:
    print(k)