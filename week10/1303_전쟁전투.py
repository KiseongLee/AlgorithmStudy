#1303_ 전쟁 - 전투
'''
처음부터 끝까지 하나도 참고 안하고 품 -> 이렇게 해야 알고리즘 공부에 도움이 될 것 같다.

문제 파악은 쉬웠음
1. 영역의 개수를 구한다(각각)
2. 어떻게 구할까? --> bfs로 구현 --> visited를 쓰면 되겠구나(bfs 함수 구현)
3. 상하좌우 돌리면서 각각의 개수를 구한다.
4. bfs 실행하기 위한 for문을 전체적으로 돌린다!
5. 예외) 상하좌우 다 다른편이고 나만 혼자일 때 -> visited가 딱 올라갈 때 체크해주면됨(시작하는 것만 따로 센다는 느낌)
6. 제곱구할 때, 코드를 줄일 수 있는 방법이 없을까?

'''

from collections import deque


n, m = map(int, input().split())

data = [list(map(str, input())) for _ in range(m)]

visited = [[0]*n for _ in range(m)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


count = 0
max_w = []
max_b = []
def bfs(x,y,color):
    
    count = 0
    global max_w, max_b
    q = deque()
    q.append([x,y,color])
    
    while q:
        
        a,b,color = q.popleft() # 이 부분이 조금 헷갈렸음, 상하좌우 다 다른편이고 나만 혼자일 때, 체크해줘야함
        if visited[a][b] ==0:
           visited[a][b] = 1
           count += 1
              
        for i in range(4):
            na = a + dx[i]
            nb = b + dy[i]
        
            if 0<=na<=m-1 and 0<=nb<=n-1:
            
             if data[na][nb] == color and visited[na][nb] == 0:
                visited[na][nb]=1
                count += 1
                q.append([na,nb,data[na][nb]])
             
                 
              
    if color == "W":
        if count != 0:
            max_w.append(count)
    else:
        if count != 0:
            max_b.append(count)
                   
for i in range(m):
    for j in range(n):
        bfs(i,j,data[i][j])

ans1 = 0
for i in range(len(max_w)):
    ans1 += max_w[i]**2

ans2 = 0
for i in range(len(max_b)):
    ans2 += max_b[i]**2

print(ans1, ans2)
