# 5분 : LCS를 뽑으면 되지 않나라는 생각이 듬 -> 개수만 구했었는데
# 10분 : 개수만 구할 수 있을듯하다는 결론이 듬
# 5분 : 참고했더니, 3차원으로 풀어야하는데 감이 안잡힘...
# 30분 : 3차원 배열로 똑같이 해주면 되는데 머릿속에 그려지진 않더라, dp를 뽑아내보고 이해해야겠다는 생각을함

L1 = input()
L2 = input()
L3 = input()

dp = [[[0]*(len(L3)+1) for _ in range(len(L2)+1)] for _ in range(len(L1)+1)]


for i in range(1, len(L1)+1):
    for j in range(1, len(L2)+1):
        for k in range(1, len(L3)+1):
            
            if L1[i-1] == L2[j-1] == L3[k-1]:
                dp[i][j][k] = dp[i-1][j-1][k-1] + 1
            else:
                dp[i][j][k] = max(dp[i-1][j][k],dp[i][j-1][k],dp[i][j][k-1])

for i in range(len(dp)):
    print(dp[i])
print(dp[-1][-1][-1])