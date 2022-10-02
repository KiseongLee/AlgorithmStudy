n,k=map(int,input().split())
num=[]
for i in range(1,n+1):
    num.append(i)
print(num)
results =[]
result = [0]*k

def dfs(L , BW):
    
    if L == k:
        results.append(result)
        return
        
    for i in range(BW, len(num)):
        result[L]=num[i]
        dfs(L+1, i+1)

dfs(0,0)
print(results)