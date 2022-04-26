import sys
input = sys.stdin.readline

n = int(input())
path = [list(map(int, input().split())) for i in range(n)]
dp = [[0]*(1<<n) for i in range(n)] # (1<<n)을 통해 방문한 도시 집합에 대응 # range(n)을 통해 도시의 개수에 대응
# dp는 내가 현재에 와있을 때, 나중에 도착지까지의 최솟값을 표시한 TABLE
max_size = sys.maxsize
# now = 현재 위치
# trace = 방문 확인
def go(now, trace):
    
    # dp값에 이미 있으면 다시 해줄 필요가 없으므로 바로 return
    if dp[now][trace]:
        return dp[now][trace]
    
    # 모든 도시를 방문했다면
    if trace == (1<<n)-1:
        # 0으로 무조건 가야하므로 현재에서 0으로 가는 값을 받아온다.
       return path[now][0] if path[now][0] > 0 else max_size
    
    cost = max_size    
    # n개의 도시를 방문해야한다. 하지만 첫 번째는 아니므로 1번부터 시작하자
    for i in range(1, n):
        # 방문을 했는가 ? / 다음으로 가는 곳의 cost가 있는가? 둘다 만족하면
        if not trace & (1<<i) and path[now][i] > 0:
            
            # 방문을 시작한다 --> 재귀로 구현 / 다음 출발지인 i가 now가 되고, 방문처리를 해주고 넘겨주면된다.
            # 이거 dp 값을 받아오는 것이기 때문에 거꾸로 생각을 해야한다. 뒤에서부터 더해준다고 생각하면 된다.
            val = go(i, trace | (1<<i))
            # 비용은 path[now][i]값을 현재 val에 더해주면 되겠다. --> 계속 갱신을 위해 min을 준다.
            # dp 값에다가 (현재 와있는 곳(i)에서 나중 도착지까지의 최솟값) now에서 i값을 더해주면 되겠다.
            cost = min(cost, val + path[now][i])
        
    
    # dp는 내가 현재 와있는 곳에서 나중 도착지까지의 최솟값을 표시한 TABLE
    dp[now][trace] = cost
    return  dp[now][trace]


print(go(0, 1))