import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

def calpath(graph, status):
    count = 0
    visited = set()
    
    def dfs(v):                      # 주변 인접 실내 개수 세기 dfs로 구현
        cnt = 0
        for ad in graph[v]:          # ad 인접한 것들, v는 노드 번호
            if status[ad] == 1:      # 인접한 것들이 실내면 카운트 + 1
                cnt += 1
            else:                     # 인접한 것들이 야외고(0이면)
                if not ad in visited: # visited에 없으면
                    visited.add(ad)   # 인접한 야외 노드 들을 visited에 넣어준다
                    cnt += dfs(ad)    # 카운트에 야외 기준으로 dfs돌린 것들을 카운트에 더해준다.
        return cnt                    # 카운트 값으로 return을 받음
    
    for i in range(1, n+1):           # 각 실내별 인접한 실내 구하기
        if status[i] == 1:
            for j in graph[i]:
                if status[j] == 1:
                    count += 1
    
        else:                         # 인접한 실외를 한 덩어리로 보고 그 덩어리에 인접한 실내의 수를 구한 뒤,
            if i not in visited:      # 각 덩어리별로 n*(n-1)의 경우의 수로 계산
                visited.add(i)
                tmp = dfs(i)
                count += tmp * (tmp-1)

    return count


n = int(input())
 
status = list(map(int, list("0"+input().strip())))      # 붙어있는 숫자 리스트로 받는 방법 그리고 0값도 추가하는 법 알아놓기!

graph = [[] for i in range(n+1)]

for i in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

print(calpath(graph, status))