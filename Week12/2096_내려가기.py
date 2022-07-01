

# n = int(input())

# data = [list(map(int, input().split())) for _ in range(n)]
# dp = [[0]*3 for _ in range(n)]
# dp2 = [[0]*3 for _ in range(n)]
# dp[0][0] = data[0][0]
# dp[0][1] = data[0][1]
# dp[0][2] = data[0][2]

# dp2[0][0] = data[0][0]
# dp2[0][1] = data[0][1]
# dp2[0][2] = data[0][2]

# if n>=2:
#     for i in range(1, n):
#         dp[i][0] = max(dp[i-1][0]+data[i][0], dp[i-1][1]+data[i][0])
#         dp[i][1] = max(dp[i-1][0]+data[i][1], dp[i-1][1]+data[i][1], dp[i-1][2]+data[i][1])
#         dp[i][2] = max(dp[i-1][1]+data[i][2], dp[i-1][2]+data[i][2])

# if n>=2:
#     for i in range(1, n):
#         dp2[i][0] = min(dp2[i-1][0]+data[i][0], dp2[i-1][1]+data[i][0])
#         dp2[i][1] = min(dp2[i-1][0]+data[i][1], dp2[i-1][1]+data[i][1], dp[i-1][2]+data[i][1])
#         dp2[i][2] = min(dp2[i-1][1]+data[i][2], dp2[i-1][2]+data[i][2])

# # print(dp, dp2)
# print(max(dp[n-1]), min(dp2[n-1]))



import sys
input = sys.stdin.readline
n = int(input())

dp_max = [0]*3
dp_min = [0]*3

dp_max_temp = [0]*3
dp_min_temp = [0]*3

for i in range(n):
    a, b, c = map(int, input().split())
    
    dp_max_temp[0] = a + max(dp_max[0], dp_max[1])
    dp_max_temp[1] = b + max(dp_max[0], dp_max[1], dp_max[2])
    dp_max_temp[2] = c + max(dp_max[1], dp_max[2])

   
    dp_min_temp[0] = a + min(dp_min[0], dp_min[1])
    dp_min_temp[1] = b + min(dp_min[0], dp_min[1], dp_min[2])
    dp_min_temp[2] = c + min(dp_min[1], dp_min[2])

    for i in range(3):
        dp_max[i] = dp_max_temp[i]
        dp_min[i] = dp_min_temp[i]
        
print(max(dp_max), min(dp_min))

