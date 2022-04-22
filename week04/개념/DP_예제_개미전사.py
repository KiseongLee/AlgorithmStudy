import sys
input = sys.stdin.readline
n = int(input())

data = list(map(int, list(input().split()))) 
data.insert(0,0)

d = [0] * 101

d[1] = data[1]
d[2] = max(data[1],data[2])         # 테스트 케이스 
                        # 2
                        # 9999 2
                        # 넣으면 data[2]는 둘 중에 큰 것을 뽑아내야하므로 d[2] = max(data[1], data[2])가 된다.

for i in range(3, n+1):
    
    d[i] = max(d[i-1], d[i-2]+data[i])

print(d[n])





'''
n = int(input())

data = list(map(int, input().split()))

dp = [0] * (n)

dp[0] = data[0]
dp[1] = max(data[0], data[1])

for i in range(2, n):
    dp[i] = max(dp[i-1], dp[i-2]+data[i])

print(dp[n-1])

이 문제도 마찬가지로 결국에는 dp 테이블을 for문으로 처음부터 초기화를 해주는 것이 핵심이고
max 값만 찾아주면되서 간단하게 풀 수 있다.
'''


