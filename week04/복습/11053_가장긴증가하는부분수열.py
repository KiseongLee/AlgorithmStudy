n = int(input())

data = [0] + list(map(int, input().split()))


dp = [1] * (n+1)
dp[1] = 1
for i in range(2, n+1):
    for j in range(1, i+1):
        if data[i] > data[j]:
            dp[i] = max(dp[i], dp[j]+1)
    
print(dp)
print(max(dp))

# 점화식을 쓰는 부분이 어려움

# key1
# 현재값을 비교해주는 이유는?

# 다 비교해주다 보니 헷갈릴 수 있는데
# 예제
# 10 20 10 30 20 50 을 보자
# 10은 20(인덱스 2)보다 작으므로 dp 업데이트
# 10은 10(인덱스 3)보다 안작고, 20도 안작으니 조건문으로 들어갈 수 없고
# 그렇게 되면 dp는 초기화 되지 않는다.
# 그래서 다음 값을 이제 시작하면 30(인덱스 4)그러면 dp를 가장 가까운것으로 계산하려고 하면
# 문제가 발생할 수 있다. 그래서 max(dp[i])를 꼭 넣어줘야한다

# key2
# 초기값을 0으로 놓으면 틀린다 왜그러지?
# 80 56 60 넣으면
# dp = [1, 0 , 1] --> 초기값 0넣으면
# dp = [1, 1, 2] -- > 초기값 1넣으면
# 답은 당연히 2이다.
# 이게 당연한 것이 0이 나올 수가 없기 때문이다 아무리 자신보다 앞쪽에 다 크더라도 dp값은 1을 가져야한다.

