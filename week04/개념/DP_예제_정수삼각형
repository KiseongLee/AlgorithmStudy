import copy
n = int(input())

data = []
for i in range(n):
    data.append(list(map(int, input().split())))

dp = copy.deepcopy(data)
# dp 테이블에 결과를 담을 것이기 때문에 크기가 같아야해서 복사를 함.


for i in range(1, n):
    # i는 행을 뜻하므로 1부터 n-1까지
    for j in range(i+1):
        # j는 열을 뜻하므로 0부터 i까지 필요하다
        if j == 0 :
            # j가 0일 때는 바로 위의 값 밖에 오지 못하기 때문에 따로 빼준다 = dp[i-1][j]
            dp[i][j] = data[i][j] + dp[i-1][j]
        elif j == i:
            # j가 i일 떄는 바로 위의 값 밖에 오지 못하기 때문에 따로 빼준다 = dp[i-1][j-1]
            dp[i][j] = data[i][j] + dp[i-1][j-1]
        
        else:
            # 위에 2개의 값과 비교를해서 큰 값이 와야하기 때문에 max로 값을 비교해줘서 넣어준다.
            dp[i][j] = data[i][j] + max(dp[i-1][j-1], dp[i-1][j])

result = 0
for i in range(n):
    # 맨 밑에 행의 값들 중 가장 큰 값을 출력하면 정답
    result = max(result, dp[n-1][i])

print(result)


#정답 풀이

n = int(input())
dp = []

for _ in range(n):
    dp.append(list(map(int, input().split())))
# 초기 데이터를 담는 변수를 사용하지 않고, 바로 dp 테이블에 초기 데이터를 담아 점화식에 따라 dp 테이블 갱신가능.

for i in range(1, n):
    for j in range(i+1):
        #왼쪽 위에서 내려오는 경우
        if j == 0:
            up_left = 0
        else:
            up_left = dp[i-1][j-1]
        #바로 위에서 내려오는 경우
        if j == i:
            up_right = 0
        else:
            up_right = dp[i-1][j]
        
        dp[i][j] = dp[i][j] + max(up_left, up_right)
        
print(max(dp[n-1]))