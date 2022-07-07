# 상자 넣기
# dp 문제
# data를 받아서 앞에 것과 비교를 해야한다 -> 앞의 인덱스를 다 확인해야하는 것이 핵심!!
# 기존의 앞의 것 하나만 비교하면 예외 케이스가 발생한다 -> 예제 1번을 넣어보면된다
# 그래서 앞에 것들 중에 나보다 작은 값을 가진 것들로 비교를 해주면 된다
# 조금 헤맨 부분이 있으면 
# 초기화를 1로 해줘야한다 상자의 개수를 구하는 것이기 때문에 그래서 계속 8%에서 틀렸습니다 나옴


n = int(input())

data = [0] + list(map(int, input().split()))

dp = [1]*(n+1) # 초기화를 1로 해야함

for i in range(2, n+1):
    for j in range(1, i):   
        if data[j] < data[i]:
           dp[i] = max(dp[i], dp[j]+1)

    

print(max(dp))
print(dp)