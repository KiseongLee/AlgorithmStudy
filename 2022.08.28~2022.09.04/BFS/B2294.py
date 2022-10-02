from collections import deque

n, k = map(int, input().split())
coins=[]
for i in range(n):
    coins.append(int(input()))
result=[]
check = [0 for _ in range(k+1)]
def bfs(target, use):
    
    queue = deque([(target, use)])
    while queue:
        target, use = queue.popleft()
        
        if target<0:
            continue
        if target == 0:
            result.append(use)
        for coin in coins:
            if coin > target:
                continue
            new_target = target - coin
            if new_target >=0 and not check[new_target]:
                check[new_target]=1
                queue.append((new_target, use+1))
bfs(k, 0)
if result:
    print(min(result))
else:
    print(-1)