
# 대문자로 다 바꾼다
# 겹치는 걸  다 뺀다
# count로 개수를 정의한다.
# 가장 큰 것을 값으로 내는데 똑같은게 있으면 ?

str = input()

str = str.upper()

str_A = list(set(str))

count_dict = {}
for A in str_A:
    solution = str.count(A)
    count_dict[A] = solution

count_list=[]
for k, v in count_dict.items():
    if v == max(count_dict.values()):
        count_list.append(k)

if len(count_list) > 1:
    print("?")
else:
    print(' '.join(count_list))
    