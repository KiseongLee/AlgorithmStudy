# 비트마스킹 : 어떤 숫자에 마스크라고 불리는 비트값을 비트 연산해서 숫자의 특정 비트 구간값을 변경시키거나
# 그 값을 추출하는 등의 행위를 말한다.
# 예를 들어
# 1001 1011 1111 0101(2) (39925)라는 2진수에서 오른쪽 두 번째 구간의 4개의 비트값을 빼오고 싶다면
# 특정 마스크와 이 수를 비트 마스킹해서 추출할 수 있다.

import sys
A = []
def go(now, trace):

    if dp[now][trace]: # now는 현재 도시 trace는 몇번째 방문한 것인가
        return dp[now][trace] # dp에 이미 값이 있으면 당연히 리턴해야함  
    if trace == (1<<N)-1: # 모든 도시 방문 완료 시,
        return path[now][0] if path[now][0] > 0 else MAX
        # 마지막 도시에서 출발도시로 가는 비용 리턴
     
    cost = MAX
    for i in range(1, N):
        if not trace & (1<<i) and path[now][i]:
            # 비트 마스크를 이용한 방문 확인 
            val = go(i, trace | (1<<i))
            cost = min(cost, val+path[now][i])
    
    dp[now][trace] = cost
    return dp[now][trace]
    

N = int(input())
path = [list(map(int, input().split())) for _ in range(N)]
dp = [[0]* (1<<N) for _ in range(N)]
MAX = sys.maxsize

print(go(0,1))



# 구체적인 경로는 중요하지 않다.
# 중복 확인
