
#복습 필요!! (05.27 -> 05.28 주석 달기)

from collections import deque


places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
n = 5

def check(place):
    
    for i in range(n):
        for j in range(n):
            if place[i][j] == "P":
                if find(i,j, place) == False:
                    return False
    return True
 
def solution(places):
    ans = []
    
    for place in places:
        if check(place):
            ans.append(1)
        else:
            ans.append(0)
    return print(ans)                         
        
                   
def find(x,y, place):
    
    global n
    visited = [[0]*n for i in range(n)]
    q = deque()
    q.append((x,y))
    visited[x][y] = 1
    
    dist = 0
    while dist<2:
      for _ in range(len(q)): # q에 들어간 애가 있으면 -> dist를 하나 늘려줘서 다시 돌리는 것!
        a, b = q.popleft()
        for adj_a, adj_b in ((a+1,b), (a,b+1), (a-1,b),(a,b-1)):
            if (0<=adj_a<n and 0<=adj_b<n) and not visited[adj_a][adj_b] and place[adj_a][adj_b] != "X":
              if place[adj_a][adj_b] == "P":
                  return False
              visited[adj_a][adj_b] = 1
              q.append([adj_a, adj_b])
      dist += 1
    return True

solution(places)