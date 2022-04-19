import sys
input = sys.stdin.readline
n, m = map(int, input().split())

data = []
for i in range(n):
    data.append(int(input()))
    
count = 0
result= []
def solve(m):
    global count
    if m < 0 :
        return
    
    if m == 0:
        result.append(count)
        return
        
        
        
    for i in data:
        count += 1
        solve(m-i)
        count -= 1
        

solve(m)

if not result:
    print(-1)
else: 
    print(min(result))