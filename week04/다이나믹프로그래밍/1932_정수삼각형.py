import copy
n = int(input())


data = []
for i in range(n):
    data.append(list(map(int, input().split())))


dp = copy.deepcopy(data)

for i in range(1,n):
    for j in range(i+1):
        
        if j == 0:
            dp[i][j] = dp[i-1][j] + data[i][j]
        
        elif j == i:
            dp[i][j] = dp[i-1][j-1] + data[i][j]
        
        else:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + data[i][j]


print(max(dp[n-1]))

# if, elif 잘써야한다. if 두개로 써버리니까 틀려버림 ㅠ