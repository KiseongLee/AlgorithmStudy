lottos = list(map(int, input().split()))

win_nums = list(map(int, input().split()))

result = 0
zero = 0
for i in range(len(lottos)):
    if lottos[i] == 0:
        zero += 1
    if lottos[i] in win_nums:
        result += 1
    
    

result_ans =[]

result_ans.append(result)
result_ans.append(result+zero)


for i in range(len(result_ans)):
    if result_ans[i] == 2:
        result_ans[i] = 5
    elif result_ans[i] == 3:
        result_ans[i] = 4
    elif result_ans[i] == 4:
        result_ans[i] = 3
    elif result_ans[i] == 5:
        result_ans[i] = 2
    elif result_ans[i] == 6:
        result_ans[i] = 1
    else:
        result_ans[i] = 6

result_ans.sort()
print(result_ans)