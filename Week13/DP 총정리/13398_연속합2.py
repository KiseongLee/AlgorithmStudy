'''
# 사실 문제를 풀면서 for문을 3개 돌리면 당연히 시간초과가 날 것으로 예상했으나
# 한 번 구현해보고 싶어서 해봄
# for문의 구간 설정이 굉장히 복잡했음
n = int(input())

data = list(map(int, input().split()))


x = min(data)
data.pop(data.index(x))
dp = [0]*(len(data)+1)

value = 0
for i in range(1, len(data)+2):
    for j in range(len(data)+1-i):
        for k in range(j, j+i):
            
            value += data[k]
        dp[i] = max(dp[i], value)
        value = 0

print(max(dp))
'''

# dp 풀이
# 1. 제거하지 않았을때 / 2. 제거했을 때
# 1. 누적 합 + 더할 값 vs 더할 값 (누적 합이 음수일 수도 있기 때문에 -> 이거 생각하기 어려움)
# 2. 제거 한 것이 (이제 올 것 vs 이미 해버린 것)
# -> 앞에서 이미 제거한 것 vs 이제 올 것을 제거한 것(더해줄 것을 안더해주면 됨)
# 모든 경우를 다 커버할 수 있음

n = int(input())
data = list(map(int, input().split()))

dp = [[0]*(n) for _ in range(2)]
dp[0][0] = data[0]
dp[1][0] = -1e9 # 꼭 설정 해줘야한다!!

for i in range(1, n):
    dp[0][i] = max(dp[0][i-1]+data[i], data[i]) # 제거하지 않은 경우(누적합 + 더할값 vs 더할값)
    dp[1][i] = max(dp[1][i-1]+data[i], dp[0][i-1]) # 제거한 경우(미리 제거 한 것 vs i번째 제거)

# print(dp)
max_value = -1e9
for i in range(len(dp)):
    if max_value < max(dp[i]):
        max_value = max(dp[i])

print(max_value)