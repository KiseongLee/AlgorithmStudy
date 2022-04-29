'''
N, M = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(N)]

dp = [[0]*(M) for i in range(N)]
dp[0][0] = 1
print(field)
for i in range(N):
    for j in range(N):
        if i == N - 1 and j == N - 1: 
            print(dp[i][j])
            break

        cur_cnt = field[i][j]

        if i <= N-1: 

           next_down_cnt = field[i+1][j]

        if j <= N-1:

           next_right_cnt = field[i][j+1]


        if 0<=i+1<N and 0<= j+1 < N:   
            if cur_cnt > next_right_cnt:
                dp[i][j+1] += dp[i][j]
            if cur_cnt > next_down_cnt:
                dp[i+1][j] += dp[i][j]

for i in range(N):  
    print(dp[i])
    
'''


