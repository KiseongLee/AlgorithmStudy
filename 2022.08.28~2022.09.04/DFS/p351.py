from itertools import combinations_with_replacement

candidates=list(map(int, input().split()))
result=[]
answer=[]
k = int(input())
for i in range(1,len(candidates)+1):
    x= list(combinations_with_replacement(candidates,i))
    for i in range(len(x)):
        result.append(x[i])
# print(result)
for i in range(len(result)):
    if sum(result[i])==k:
        answer.append(list(result[i]))

print(answer)