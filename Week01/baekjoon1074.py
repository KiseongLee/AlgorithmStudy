# n = int(input())
# # r,c = map(int, input())
# visited = [[0]*(2**n) for _ in range(2**n)]

# print(visited)

# dx = [0, 1, 0, -1]
# dy = [1, -1, 1, 1]


# def dfs(x,y):
    
#    if x <= -1 or x >= (2**n) or y <= -1 or y >= (2**n):
#        return False

#    for i in range(4):
       
#        if x <= -1 or x >= (2**n) or y <= -1 or y >= (2**n):
#         return False
    
#        nx = x + dx[i]
#        ny = y + dy[i]

#        if nx <= -1 or nx >= (2**n) or ny <= -1 or ny >= (2**n):
#          return False

#        visited[nx][ny] = visited[x][y] + 1
#        x = nx
#        y = ny
    
#    dfs(x,y+1)
    
 
    

# dfs(0,0)
# print(visited)    

# #    dfs(x,y)
# #    dfs(x,y+2)
# #    dfs(x+2,y)
# #    dfs(x+2,y+2)


  
      


# # def dfs(x):

# #     global count
# #     for i in range(2**n):
# #        visited[x][i] = True
# #        count += 1
    
# #     if x <= ((2**n)*(2**n)):

# #        dfs(x+1)
    
# #     else: 
# #         return visited[x]

# # dfs(0)

# # print(visited)
    


# 1. 방문처리 불가
# 2. 배열 넣기 불가
# 3. 공식?

import sys
input = sys.stdin.readline

def recursive(size, x , y):
    global count
    if x == r and y == c:
        print(count)
        return

    if size == 1:
        count += 1
        return
    if not (x <= r < x+size and y <= c < y + size):
        count += size * size
        return
    
    recursive(size//2, x, y)
    recursive(size//2, x, y + size//2)
    recursive(size//2, x + size//2, y)
    recursive(size//2, x + size//2, y + size//2)

n, r, c = map(int, input().split())

count = 0
recursive(2**n, 0, 0)