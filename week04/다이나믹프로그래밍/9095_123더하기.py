# dfs로 풀 때는 순열로 풀어져서 순서를 다 체크할 수 있게 된다 
# 다이나믹 프로그래밍으로는 조합으로만 풀 수 있었다 동전1 문제에서
# 그렇다면 어떻게 풀 수 있는지 확인해보자


'''
t = int(input())

count = 0
def dfs(x):
    global count
    if x == 0:
        count +=1
        return
    
    if x < 0 :
        return
    
    for i in range(1, 4):
        dfs(x - i)
    

for i in range(t):
    n = int(input())
    dfs(n)
    print(count)
    count = 0
'''

t = int(input())

for i in range(t):
    n = int(input())
    dp = [0]*(n+1)
    
    dp[1] = 1
    if n>= 2:
      dp[2] = 2
    if n>=3 :
        dp[3] = 4
    for i in range(4, n+1):
        dp[i] = dp[i-3] + dp[i-2] + dp[i-1]
        # 핵심 key : 3을 빼는 것은 dp[i-3]에 3을 더해서 만들 수 있는 가지 수를 더해주고
        #           2를 빼는 것은 dp[i-2]에 2를 더해서 만들 수 있는 가지 수를 더해주고
        #           1을 빼는 것은 dp[i-1]에 1를 더해서 만들 수 있는 가지 수를 더해주는 것이다.
    print(dp[n])
    