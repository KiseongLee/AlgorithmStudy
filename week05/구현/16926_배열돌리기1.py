n, m, r = map(int, input().split())

d = [list(map(int, input().split())) for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


for i in range(r):
    
  for k in range(min(m,n)//2):
      x,y = k, k
      cnt = 0
      cur_value = d[x][y]
      for i in range(4):
        
        if i == 0 or i == 2:
            b = n - cnt
        if i == 1 or i == 3:
            b = m - cnt
            
        for j in range(k+1, n-k): 
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx > n-1 or ny > n-1:
                continue
            
            prev_value = d[nx][ny]
            d[nx][ny] = cur_value
            cur_value = prev_value
            x = nx
            y = ny
            
      cnt +=2

for i in range(n):
    print(d[i])
    
# 하나씩 밀리면서 가야하는데 나는 값이 바뀌어버리므로 틀림
# 값이 바뀌기만 하네 
# 어떻게 구현해야할까?
# 1시간 소요.. 답을 확인하거나 힌트를 받아야할 듯
