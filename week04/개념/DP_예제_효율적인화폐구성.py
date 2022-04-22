n, m = map(int, input().split())

data = []
for i in range(n):
    data.append(int(input()))

d = [10001]*(m+1)

d[0] = 0

for i in range(n):
    for j in range(data[i], m+1):
        if d[j - data[i]] != 10001:
            d[j] = min(d[j], d[j - data[i]]+1)


if d[m] == 10001:
    print(-1)
else:
    print(d[m])
    
    
    

# 이 문제도 결국에는 dp 테이블을 하나씩 갱신해나가는 것이 문제인데
# 여기서 헷갈리는 건 빼기가 0이 되어야 내가 만들 수 있는 화폐라는 것이고
# dp[0]을 활용해야하는 것이다 // dp[0] = 0이 되어야한다.