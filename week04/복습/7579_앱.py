import sys
input = sys.stdin.readline
n, m = map(int, input().split())


memory = list(map(int, input().split()))
cost = list(map(int, input().split()))

data =[]
for i in range(n):
    data.append((memory[i], cost[i]))

data.sort()
    

dp = [0] * (sum(cost)+1)    #i값이 정확히 비용이기 때문에 +1을 더해줘야함!!
                            # 아래와 같은 반례가 있을 수 있기 때문에

for j in range(len(data)): 
  for i in range(len(dp)-1, data[j][1]-1, -1):
      dp[i] = max(dp[i], dp[i-data[j][1]]+data[j][0])



for i in range(len(dp)):
    
    if dp[i] >= m:
        print(i)
        break

'''
5 10000000
9999999 9999999 9999999 9999999 9999999
2 1 3 4 5
정답 : 3

10 10
1 1 1 1 1 1 1 1 1 1
10 10 10 10 10 10 10 10 10 10
정답 : 100
'''