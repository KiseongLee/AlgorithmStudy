from collections import deque

n = int(input())
k = int(input())

d = [[0]*(n+1) for _ in range(n+1)]

for i in range(k):
    a,b = map(int, input().split())
    
    d[a][b] = 1

change={}
l = int(input())
for i in range(l):
    sec, direc = input().split()
    sec = int(sec)
    change[sec] = direc 

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

direction = 0
count = 0



def map(x,y):
    global count, direction, sec, direc
    
    q = deque()
    q.append((x,y))
    nx = x
    ny = y
    
    while True:
        
        if d[x][y] != 1:
        
            x,y = q.popleft()
            
            if count in change.keys():
                if change[count]=="D":
                    turn_right()
                                
            else:
                    turn_left()
                    
            nx += dx[direction]
            ny += dy[direction]

            if nx > n or ny > n or nx <= 0 or ny <= 0 or (x == nx and y == ny):
                    count += 1
                    break
                    
            x = nx
            y = ny
            
            if not (x, y) in q:
                 q.append((x,y))
                 count += 1

            else:
                break
            
        else:
            
            d[x][y] = 0
            
            if count in change.keys():
                if change[count]=="D":
                    turn_right()
                                
            else:
                    turn_left()
                    
            nx += dx[direction]
            ny += dy[direction]
            
            if nx > n or ny > n or nx <= 0 or ny <= 0 or (x == nx and y == ny):
                    count += 1
                    break
         
            x = nx
            y = ny
 
            if not (x, y) in q:
                q.append((x,y))
                count += 1
                

            else:
                break
            
    return count
            
        

def turn_left():
    global direction
    direction += 1
    if direction == 4:
        direction = 0
    
def turn_right():
    global direction
    direction -= 1
    if direction == -4:
        direction = 0


print(map(1,1))



