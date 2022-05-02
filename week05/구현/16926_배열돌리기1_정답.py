import sys
input = sys.stdin.readline
n, m, r = map(int, input().split())

d = [list(map(int, input().split())) for _ in range(n)]

for _ in range(r):
    
    for i in range(min(n,m)//2):
        s_x, s_y = i, i
        cur_value = d[s_x][s_y]
        
        for j in range(i+1, n-i):
            s_x = j
            prev_value = d[s_x][s_y]
            d[s_x][s_y] = cur_value
            cur_value = prev_value
            
        for j in range(i+1, m-i):
            s_y = j
            prev_value = d[s_x][s_y]
            d[s_x][s_y] = cur_value
            cur_value = prev_value
        
        for j in range(i+1, n-i):
            s_x = n - j - 1
            prev_value = d[s_x][s_y]
            d[s_x][s_y] = cur_value
            cur_value = prev_value
            
        for j in range(i+1, m-i):
            s_y = m - j - 1
            prev_value = d[s_x][s_y]
            d[s_x][s_y] = cur_value
            cur_value = prev_value
            
for i in range(n):
    for j in range(m):
        print(d[i][j], end=' ')
    print()