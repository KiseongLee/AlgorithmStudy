n = int(input())

data = list(map(int, input().split()))

dp = [1]*(n)

for i in range(1, n):
    for j in range(i):
        if data[i] < data[j]:
            dp[i] = max(dp[i], dp[j]+1)             # 6 / 1 6 5 7 2 4 넣으면 dp의 순을 보면 max가 왜 들어가야하는지 알 수 있다.
            
print(max(dp)) # 이걸로 출력해야 답임
print(dp[n-1]) # 이걸로 출력하면 틀림

# 끝값이 가장 크면 문제가 발생하지 갱신이 안되는데 ....
# 반례
# 7
# 8 7 9 5 4 3 11
# print(max(dp)) 5
# print(dp[n-1]) 1