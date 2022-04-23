'''
n = int(input())

data = []
data.append([0])
for i in range(n):
    
    data.append(list(map(int, input().split())))

# for i in range(3):

#     min_value = 1001
#     cnt = 0
#     for j in range(1, n+1):
        
#         if min_value >= data[j][i]:
#             min_value = data[j][i]
#             cnt +=1
#         if cnt >= 2:
#             data[1][i] = 1001

dp = [0] * (n+1)
dp[1] = min(data[1])
idx = data[1].index(min(data[1]))

for i in range(2, n+1):
    data[i][idx] = 1001
    dp[i] = dp[i-1] + min(data[i])
    idx = data[i].index(min(data[i]))

print(dp[n])

# 구현은 했지만, 설계가 틀렸다.
# 점화식이 조금 부족하다 싶었는데 역시나 틀렸다.
# 어떻게 다시 보완해야할까

'''
# 반례
# 3
# 1 9 2 
# 1 9 9
# 9 1 9

# 출력 : 19
# 답 : 4

'''
'''
n = int(input())

data = []
for i in range(n):  
    data.append(list(map(int, input().split())))


for i in range(1, n):
    data[i][0] = min(data[i-1][1], data[i-1][2]) + data[i][0]
    data[i][1] = min(data[i-1][0], data[i-1][2]) + data[i][1]
    data[i][2] = min(data[i-1][0], data[i-1][1]) + data[i][2]

print(min(data[n-1]))