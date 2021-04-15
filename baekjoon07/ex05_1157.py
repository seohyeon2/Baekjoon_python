# 1157번 : 단어 공부

original_word = input().upper()
new_word = list(set(original_word))

cnt_list = []
for i in new_word:
    cnt = original_word.count(i)
    cnt_list.append(cnt)
if cnt_list.count(max(cnt_list)) >= 2 :
    print("?")
else:
    print(new_word[(cnt_list.index(max(cnt_list)))])