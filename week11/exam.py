
user_id =["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id =["fr*d*", "*rodo", "******", "******"]

from itertools import product

flag = True
ans = []
for i in range(len(banned_id)):
    for j in range(len(user_id)):
        k=0
        flag = True
        while flag:
            
            if k == len(banned_id[i]):
               ans.append([user_id[j], i])
               break
            
            if len(user_id[j])!=len(banned_id[i]):
                flag = False

            if user_id[j][k] == banned_id[i][k] or banned_id[i][k]== "*":
                k += 1
                continue
            else:
                break
            

ans2 =[[] for _ in range(len(banned_id))]
for  j in range(len(ans)):
    for i in range(len(banned_id)):
        if ans[j][1] == i:
           ans2[i].append(ans[j][0])


X = list(product(*ans2))

Y=[]
for i in range(len(X)):
     Z = set(X[i])
     Y.append(tuple(Z))

ans3 = []
for i in range(len(Y)):
    if len(Y[i]) == len(banned_id):
        ans3.append(Y[i])

A = set(ans3)
ans3 = list(A)
print(ans3)
print(len(ans3))


