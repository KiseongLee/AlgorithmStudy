# 10 분 : 전에 풀었던 펠린드롬 만들기(1254) 문제를 떠올림 -> 근데 문제는 이것은 문자열이었고 지금 문제는 정수
# 10 분 : 아마 dp를 사용해야하므로 어떻게 점화식을 구성할지 떠올려보자 -> 17분 경과 아무것도 못알아냄 -> 질문체크?
# 10 분 : 힌트 참고
# 10 분 : LCS랑 비슷하다고 하는데 확인해보자
# 10 분 : 구현 중(LCS)


n = int(input())
X= list(map(int, input().split()))


dp =[[0]*(n+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        if  X[j-1] == X[-i]:
            dp[i][j] = dp[i-1][j-1]+1
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])
            

# 시간이 많이 차이나네.. 위에처럼 풀자!!
# n = int(input())
# X = list(map(int, input().split()))
# Y=X[::-1]

# X = [0]+X
# Y = [0]+Y

# dp = [[0]*(n+1) for _ in range(n+1)]

# for i in range(1, len(X)):
#     for j in range(1, len(Y)):
#         if X[i] == Y[j]:
#             dp[i][j] = dp[i-1][j-1] + 1
#         else:
#             dp[i][j] = max(dp[i-1][j], dp[i][j-1])

# # for i in range(len(dp)):
# #     print(dp[i])

# print(n - dp[-1][-1])

