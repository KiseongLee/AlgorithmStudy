n = int(input())

T = [0]
P = [0]



for i in range(n):
    a, b = map(int, input().split())
    T.append(a)
    P.append(b)

DP = [0]*(n+2)

max_value = 0
for i in range(n, 0, -1):
    if T[i]+i <= n+1:                   # 마지막날은 카운팅을 해야 하니까 =값이 붙는 것이다.
        DP[i] = max(P[i]+DP[T[i]+i], max_value)
        max_value = DP[i]
    
    else:
        DP[i] = max_value
        
    

print(max(DP))

# 박살남, 문제가 어렵고 헷갈림, 점화식도 헷갈리는데 마지막 값 처리 때문에 더 헷갈림 어떻게 처리해주는지 
# 잘 봐야함

# n = int(input())
# t = []
# p = []
# dp = [0] * (n+1)
# max_value = 0

# for _ in range(n):
#     x,y = map(int, input().split())
#     t.append(x)
#     p.append(y)

# for i in range(n-1, -1, -1):
#     time = t[i] + i
    
#     if time <= n:
#         dp[i] = max(p[i]+ dp[time], max_value)
#         max_value = dp[i]
    
#     else:
#         dp[i] = max_value

# print(max(dp))