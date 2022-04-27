n = int(input())
INF = 1e9
dp = [INF] * (n+1)
dp[1] = 0
result = [0] * (n+1)
ans =[]
for i in range(2,n+1):
    
    dp[i] = dp[i-1]+1
    result[i]=i-1
    
    if i % 2 == 0 and dp[i] > dp[i//2] + 1:
        dp[i] = dp[i//2]+1
        result[i] = i//2
    if i % 3 == 0 and dp[i] > dp[i//3] + 1:
        dp[i] = dp[i//3]+1
        result[i] = i//3

print(dp[-1])

while n != 0:
    
    print(n, end=' ')
    n = result[n]


# 뽑아내는 것이 어려움 --> 값을 잘 보고 판단해야함
# n 자체를 프린트하고 그다음에 바로 배열에 넣고 돌리면 되잖아
# 생각을 잘하자
