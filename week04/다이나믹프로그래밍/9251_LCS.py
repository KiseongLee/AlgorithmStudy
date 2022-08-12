
X= [0]+list(input())
Y = [0] + list(input())

dp =[[0]*(len(Y)) for _ in range(len(X))]

for i in range(1, len(X)):
    for j in range(1, len(Y)):
        if X[i] == Y[j]:
            dp[i][j] = dp[i-1][j-1]+1
            # j를 j-1로 만들어야 답이 된다. 왜??
            # ABAA / AABB를 넣어보면 된다
            # 세번 째, A가 들어갔을 때, 2가 되면 안되는데 j를 넣으면 되버린다. 그래서 문제가 생긴다.
            # 추가 됨과 동시에 더해줘야하는거지. 추가 됨과 동시에 더해준다!!
            
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])
            
for i in range(len(dp)):
    print(dp[i])

print(dp[-1][-1])


