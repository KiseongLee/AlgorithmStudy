import sys
input = sys.stdin.readline

n, m = map(int, input().split())

data = []
for i in range(n):
    data.append(int(input()))
INF = int(1e9)
min_value = INF
count = 0
result= []
def solve(m):
    global count, min_value
    if m < 0 :
        return
    
    if m == 0:
        if min_value > count:
           min_value = count
           return 
        
        
        
    for i in data:
        count += 1
        solve(m-i)
        count -= 1
        
solve(m)

if min_value == INF:
    print(-1)
else:
    print(min_value)

