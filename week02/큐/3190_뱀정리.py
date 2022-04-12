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
x,y = 1,1
direction = 0                   # 첫 방향은 오른쪽(+y) 방향이므로 0부터 시작


def turn_left():                # 방향 전환(왼쪽)
    global direction
    direction += 1
    if direction == 4:
        direction = 0
    
def turn_right():               # 방향 전환(오른쪽)
    global direction
    direction -= 1
    if direction == -4:
        direction = 0


q = deque()
q.append((x,y))                 # 처음 시작점 deque에 넣어주기


def boundary_check(x,y):
    if 1 <= x <n+1 and 1<= y < n+1:   # 왜 n을 포함하지 않을까? n까지는 올 수 있는 것 아닌가?
        return True
    return False
    


count = 0

  
while True:
     
   count += 1                           # 초 카운트 해주기
   nx = x + dx[direction]               # 방향 설정 x좌표
   ny = y + dy[direction]               # 방향 설정 y좌표
   
   if count in change.keys():           # 방향전환 딕셔너리 사용 // 8 D 라고 했을 때
        if change[count]=="D":          # count 8일 때, change[8] = D 이면 오른쪽 회전
            turn_right()
        else:
            turn_left()                 # 아니면 왼쪽 회전
        
   if boundary_check(nx, ny):           # 바운더리 체크 범위 안에 들어오고
       if (nx, ny) in q:                # 그런데 큐안에 이미 좌표가 있으면 종료
          break
    
       if d[nx][ny] == 1:               # 방문한 곳에 사과가 있으면
           q.append((nx,ny))            # 큐에 값을 넣어주면서 길이가 1증가하고
           d[nx][ny] = 0                # map에서 1을 0으로 바꿔준다
        
       else:
           q.append((nx, ny))           # 없으면 큐에 값을 넣어주면서
           q.popleft()                  # 꼬리를 없애자
        
       x, y = nx, ny                    # x, y nx,ny로 초기화해야 계속 넘어가겠지
       
   else:
        break       
       
            
    

print(count)



