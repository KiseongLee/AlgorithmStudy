# n = int(input())

'''
matrix = [list(map(int, input().split())) for _ in range(n)]
# 곱셈의 최소 횟수 행렬
dp = [[0]*n for _ in range(n)]
#dp[i][j] = 행렬을 곱하는데 필요한 곱셈의 최소 횟수를 담은 배열
# matrix[i]에서 matrix[j]까지 행렬을 곱하는데 필요한 곱셈의 최소 횟수

for diagonal in range(1, n): # dp[i][i]는 자기 자신의 행렬이기 떄문에 값이 0
    for i in range(0, n-diagonal): # 대각선의 우측 한 칸 씩 이동
        j = i + diagonal # 현재 대각선에서 몇 번째 원소인지
        # 차이가 1밖에 나지 않는 칸
        if diagonal == 1:
            dp[i][j] = matrix[i][0] * matrix[j][0] * matrix[j][1]
            continue
        
        dp[i][j] = 2**31
        # 각 부분행렬 곱셈 횟수 + 두 행렬의 곱셈 횟수
        for k in range(i, j): # k값으로 최적 분할 찾기
            dp[i][j] = min(dp[i][j], dp[i][k]+ dp[k+1][j]+ matrix[i][0]*matrix[k][1]*matrix[j][1])
  '''          
#https://dapsu-startup.tistory.com/57

import sys
input = sys.stdin.readline
n = int(input())
mat = [tuple(map(int, input().split())) for i in range(n)]

dp = [[0]*n for i in range(n)]
for cnt in range(n-1):
    for i in range(n-1-cnt):
        j = i+cnt+1
        dp[i][j] = 2**31
        for k in range(i, j):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + mat[i][0]*mat[k][1]*mat[j][1])
print(dp[0][-1])

# https://ddiyeon.tistory.com/72