'''
1. 방문 처리 해주고

2. 색깔 처리 해주면 되는데

색깔 처리를 할 때, 앞에 것을 받아오고 비교를 해야하는데 어떻게 진행.



'''

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def dfs(graph, v, idx, visited, checked):       # dfs 시작
        global ans, flag                        # ans = 출력 담을 list, flag = No가 나올 때, 재귀함수 종료 용도
        
        visited[v] = True                       # 방문한 노드 방문처리
        if checked[idx] == 0:                   # 인접한 노드는 서로 달라야하기 때문에 checked라는 list를 만들어서 표시, idx는 재귀함수를 불러오는 인접한 노드를 표시
            checked[v] = 1                      
        else:
            checked[v] = 0                      # 인접한 노드의 checked가 1이었다면 0으로 표시
        
        
        for i in graph[v]:                      # 방문처리한 노드의 인접한 노드들 for문 동장
          if flag == 0:                         # flag(No가 나올 때 재귀함수 종료 조건)==0일 때,
            if not visited[i]:                  # 인접한 노드가 방문처리 되지 않았다면
                dfs(graph, i, v, visited, checked) # dfs 재귀함수 동작
            else:                               # 방문이 되었다면
                if checked[i] == checked[v]:    # 인접한 노드들의 checked가 갔다면 --> 이분그래프가 불가능
                   flag = 1                     # 따라서 flag를 1로 바꿔주고
                   ans.append("NO")             # NO를 출력담을 list에 담는다.
                   return                       # 함수 종료
                     

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
      if not visited[i]:                   
        dfs(graph, i, 0, visited, checked)
        checked = [0] * (v+1)
        if flag == 1:                           # 이 문제 핵심 : dfs를 1만 돌리면 안됨. 왜냐하면 연결 요소(connecte component)가 있을 수 있기 때문에
            break                               # for문으로 1부터 전체 노드의 수만큼 돌려줘야한다. 돌릴 때 마다 checked는 초기화 해줘야함
                                                # visited도 원래 초기화를 해줘야 한다!! 그런데 이 것을 넣고 돌리면 시간초과가 뜸 ㅠ
                                                # 당연히 시간초과가 뜨는게 맞다. 왜냐하면 방문 처리를 한 것들은 더 이상 갈필요가 없기 때문에
                                                # 내가 확인하고 싶은 것은 방문처리를 안한 곳이 있어서 거기만 돌면되는 거기 때문이다.
       
    if flag == 0:                               # flag가 0이면 YES를 넣어주면 된다
       ans.append("YES")
   

for i in range(len(ans)):
    print(ans[i])
    

    
'''
2
3 2
1 3
2 3
4 4
1 2
2 3
3 4
4 2

53 ~ 57 줄
  for i in range(1, v+1):
      if not visited[i]:                    
        dfs(graph, i, 0, visited, checked)
        checked = [0] * (v+1)
이걸로 대체 가능

그런데 이게 더 느림
위에 것은 바로 NO 나오자마 for문을 break하는데
밑에 것은 for문으로 한 번가서 visited를 확인하니까 느린거네

생각해보니 for문이 더 돌 필요가 없이 if not visited 까지 걸어주면 훨씬 빠를듯하다
둘이 다른 걸 없애주는 거 였다.

'''

    

    
