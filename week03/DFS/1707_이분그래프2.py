from collections import deque
import sys
input = sys.stdin.readline

def bfs(graph, start, visited, checked):
     global ans, flag
     queue = deque([start])
    
     visited[start] = True
    
     while queue:
        
        v = queue.popleft()
        
        
        for i in graph[v]:
         if flag == 0:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                if checked[v] == 0:
                   checked[i] = 1
                else:
                   checked[i] = 0
            else:
                if checked[i] == checked[v]:
                    flag = 1
                    ans.append("NO")
                    return



k = int(input())                                # 테스트 케이스

ans = []                                        # 출력 담을 list

for i in range(k):
    
    flag = 0                                    # flag는 계속 초기화 해줘야하기 때문에 for문 안에 넣음
    v,e = map(int, input().split())
    graph = [[] for i in range(v+1)]
    visited = [False] * (v+1)                   # 인덱스 0은 사용하지 않으므로 v+1개 만듬
    checked = [0] * (v+1)                       # 인덱스 0은 사용하지 않으므로 v+1개 만듬
    for i in range(e):                          # 간선(edge)들의 내용을 받음
        a,b = map(int, input().split())         
        graph[a].append(b)                      # 방향이 없으므로 양쪽에 넣어줘야한다.
        graph[b].append(a)
    
    for i in range(1, v+1):  
      if not visited[i]:                        # 이 문제 핵심 : dfs를 1만 돌리면 안됨. 왜냐하면 연결 요소(connecte component)가 있을 수 있기 때문에
       checked = [0] * (v+1)                    # for문으로 1부터 전체 노드의 수만큼 돌려줘야한다. 돌릴 때 마다 checked는 초기화 해줘야함
                                                # visited도 원래 초기화를 해줘야 한다!! 그런데 이 것을 넣고 돌리면 시간초과가 뜸 ㅠ
       bfs(graph, i, visited, checked)
       if flag == 1:
           break
       
    if flag == 0:                               # flag가 0이면 YES를 넣어주면 된다
       ans.append("YES")

for i in range(len(ans)):
    print(ans[i])
    
    

'''
11                       
3 1
2 3
3 2
1 3
2 3
4 4
1 2
2 3
3 4
4 2
3 2
2 1
3 2
4 4
2 1
3 2
4 3
4 1
5 2
1 5
1 2
5 2
1 2
2 5
4 3
1 2
4 3
2 3
4 4
2 3
1 4
3 4
1 2
3 3
1 2
2 3
3 1
2 1
1 2
YES
YES
NO
YES
YES
YES
YES
YES
YES
NO
YES

'''