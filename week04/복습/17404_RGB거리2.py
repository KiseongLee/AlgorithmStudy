# n = int(input())

# data = []
# for i in range(n):
#     data.append(list(map(int, input().split())))

# max = 1001

# dp = [[0]*3 for i in range(n)]
# index =[]
# for i in range(3):
#     dp[0][i] = data[0][i]


# dp[1][0] = data[1][0] + min(dp[0][1], dp[0][2])
# dp[1][1] = data[1][1] + min(dp[0][0], dp[0][2])
# dp[1][2] = data[1][2] + min(dp[0][0], dp[0][1])

# index.append(dp[0].index(min(dp[0][1], dp[0][2])))
# index.append(dp[0].index(min(dp[0][0], dp[0][2])))
# index.append(dp[0].index(min(dp[0][0], dp[0][1])))


# for i in range(2, n):
    
#     dp[i][0] = data[i][0] + min(dp[i-1][1], dp[i-1][2])
#     dp[i][1] = data[i][1] + min(dp[i-1][0], dp[i-1][2])
#     dp[i][2] = data[i][2] + min(dp[i-1][0], dp[i-1][1])
    
#     if i == n-1:
#       if index[0] == 0:
#          dp[i][0] = min(data[i][1], data[i][2]) + min(dp[i-1][1])
#       if index[1] == 1:
#           dp[i][1] = max
#       if index[2] == 2:
#           dp[i][2] = max

# print(index)
# print(dp)
# print(min(dp[n-1]))

# 실패,, 너무 복잡해졌다. index까지는 구해왔는데 여기서 처리를 어떻게 해야할지 머리속이 복잡해짐



n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
result, inf = 1e9, 1e9

for color in range(3):
    dp = [[0 for _ in range(3)] for _ in range(n)]
    for i in range(3):
        if i == color:
            dp[0][i] = data[0][i]
        else:
            dp[0][i] = inf
    
    for i in range(1, n):
        dp[i][0] = data[i][0] + min(dp[i-1][1], dp[i-1][2])
        dp[i][1] = data[i][1] + min(dp[i-1][0], dp[i-1][2])
        dp[i][2] = data[i][2] + min(dp[i-1][0], dp[i-1][1])
    
    for i in range(3):
        if i != color:
            result = min(result, dp[-1][i])
            
            
print(result)

# 아예 처음부터 색깔을 가지고 가는 방법
# 말하자면 식은 그대로 뒤에것을 가져가면서, 뒤에 확인하는 조건을 걸어주는데
# 이걸 구현할 때, for문을 통해서 구현

# 0 index에 선택하는 얘를 먼저 값을 받아놓고, 다른 것들은 INF로 해버린다.


