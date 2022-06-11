from itertools import combinations
from collections import Counter

orders = list(map(str, input().split()))

course = list(map(int, input().split()))


ans = []
ans2 = []
# ans.append(list(combinations(orders[0], course[0])))

for i in course:
    for j in range(len(orders)):
        if len(orders[j])>= i:
            ans.append(list(combinations(orders[j], i)))

# print(ans)
for i in range(len(ans)):
    for j in range(len(ans[i])):
        ans2.append(ans[i][j])

# print(ans2)
ans3 = []
for i in range(len(ans2)):
    ans3.append(''.join(sorted(ans2[i])))
# print(ans3)

ans4=[]
for i in range(len(ans3)):
    if ans3.count(ans3[i]) >= 2:
        ans4.append((ans3[i], ans3.count(ans3[i]))) 
X = set(ans4)
ans4 = list(X)
# print(ans4)

max = 0
max_idx = 0
ans5 = []
ans4 = sorted(ans4, key = lambda x : -x[1])
for i in course:
    for j in range(len(ans4)):
        if len(ans4[j][0]) == i:
            if ans4[j][1] >= max:
               max = ans4[j][1]
               max_idx = j
               ans5.append(ans4[max_idx][0])

    max=0

    
sorted(ans5)
              
        
