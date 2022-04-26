import sys
n = int(input())
path = [list(map(int, input().split())) for i in range(n)]
dp = [[0]*(1<<n) for i in range(n)]
max_size = sys.maxsize 
def go(now,trace):
    
    if dp[now][trace]:      #dp[now][trace] 값이 있다면
        return dp[now][trace] # 중복해서 계산할 필요가 없기 때문에 바로 출력

    if trace == (1<<n)-1: # 만약 trace가 모두 다 켜졌다면, 방문을 모두 했다면(비트마스킹)
        return path[now][0] if path[now][0] > 0 else max_size # 0으로 무조건 가야하므로 trace 즉 비트 마스킹이 모두 방문했다면, path[now][0] now에서 0으로 가는 값을 받아온다.
                                                              # path[now][0] = 0 이면 갈 수 없다는 것이므로 max_size로 초기화한다.
    cost = max_size # 비용은 무한대로 초기화한다 --> 최솟값을 구해야하기 때문에
                    # cost를 정의해준다.
                    
    # 방문 가능한 모든 곳에 대해서 for문 시작
    for i in range(1, n):
        if not trace & (1 << i) and path[now][i] > 0: # 현재 비트마스킹 되어 있는 것과 현재(i)를 비트마스킹 켠 것을 and 조건을 걸었을 때, 만약에 이미 켜져 있는게 있으면 1이 될 것이고 not을 걸면은 0이 되므로 False가 되어서 조건이 걸리지 않고, 
                                                      # path[now][i]는 현재에서 i로 가는 비용이 0보다 커야할 때 (0보다 작으면 값이 없는 것이기 때문에 의미가 없어진다.)
            
            #이제 방문 조건을 확인했으니, 방문을 해야한다. 방문을 어떻게하지? #재귀를 돌리면 된다.
            val = go(i, trace | 1<<i)
            #비용을 갱신해야한다. --> 최솟값으로 갱신을 계속해줘야한다.
            cost = min(cost, val + path[now][i])
            # 얘는 처음부터 방문하는 것으로 더해주는 느낌으로 쓴 식이지만, 재귀함수 때문에 뒤에서 부터 더해주는 것이 된다.
    
    #dp 값을 이제 넣어줘야겠지? dp[now][trace]는 now는 현재있는 위치 trace는 비트마스킹 방문했는지 안했는지를 체크하는 변수
    #dp는 현재까지 방문했다면 그 이후에 방문할 수 있는 모든 경우의 수에서 최소 비용을 구한 값임.
    dp[now][trace] = cost
    return dp[now][trace]

print(go(0, 1))
 

    
    