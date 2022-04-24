'''
n = int(input())
INF = int(1e9)
dp = [INF] * (n+1)

data = [3, 5]

for i in range(1,n+1):
    if i % data[0] == 0:
        dp[i] = i // data[0]


for i in range(data[1], n+1):
    if i % data[1] == 0:            # 5를 뺐는데 5의 배수인 경우
        dp[i] = i // data[1]
    if (i-data[1]) % data[0] == 0:  # 5를 뺐는데 3의 배수인 경우
        if dp[i] > dp[i-data[1]] +1:
           dp[i] = dp[i-data[1]] + 1
    if (i-data[0]) % data[0] == 0:  # 3을 뺐는데 3의 배수인 경우
        if dp[i] > dp[i-data[0]]+1:
            dp[i] = dp[i-data[0]]+1
    if (i-data[0]) % data[1] == 0:  # 3을 뺐는데 5의 배수인 경우
        if dp[i] > dp[i-data[0]] + 1:
           dp[i] = dp[i-data[0]] + 1
    if (i-data[0]*2) % data[1] == 0: # 6을 뻈는데 5의 배수인 경우
        if dp[i] > dp[i-data[0]*2] + 1:
            dp[i] = dp[i-data[0]*2] + 1
    if (i-data[1]*2) % data[0] == 0: # 10을 뻈는데 3의 배수인 경우
        if dp[i] > dp[i-data[1]*2] + 1:
            dp[i] = dp[i-data[1]*2] + 1
            
if dp[n] == INF:
    print(-1)
else:  
    print(dp[n])
'''    
# 너무 많은 반례가 나옴.. 설계를 잘못한듯

n = int(input())

dp = [5001] * (n+5)
dp[3] = dp[5] = 1

for i in range(6, n+1):
    dp[i] = min(dp[i-3],dp[i-5])+1

print(dp[n] if dp[n]<5001 else -1)
    
    
    