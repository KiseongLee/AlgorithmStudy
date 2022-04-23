# 바로 직전에 오는 것은 dp로 더해 버리면 예외조건 (3칸 연속)에 걸릴 수 있기 떄문에
# 무조건 점화식 쓸 떄, i-3 까지 써줘야한다.

# i-2에 있는 것은 바로 dp값으로 해도 된다. 어차피 올라갈 수 있는 경우는 2칸 뛰는 1가지 밖에 없어서
# 예외조건에 걸릴 수 없다. 그 전에 어떻게 올라 오든지 아무 상관이 없는 것이다.

# https://daimhada.tistory.com/181

n = int(input())

data = [0]
for i in range(n):
    data.append(int(input()))
    
dp = [0] * (n+1)


dp[1] = data[1]

if n >= 2:
   dp[2] = data[1] + data[2]
if n >= 3:
   dp[3] = max(data[1]+data[3], data[2]+data[3])

for i in range(4, n+1):
    dp[i] = max(dp[i-3]+data[i-1]+data[i], dp[i-2]+data[i])

print(dp[n])
print(dp)
