# 문제를 잘 확인하자 // L값이 어디에 주어져있는지 한참 확인함
# 문제를 잘 읽고 구현을 해야함 // 조건이 다 주어져있음

n, l = map(int, input().split())

data = [list(map(int, input().split())) for _ in range(n)]

result = 0

def check(now):
    for j in range(1,n):
        if abs(now[j] - now[j-1]) > 1:
            return False                            #  2번 조건
    

        if now[j] < now[j-1]:
            
            for k in range(l):
                if j+k >= n or visited[j+k] or now[j] != now[j+k]:  # 1, 3, 4 조건
                    return False
            
                if now[j] == now[j+k]:
                    visited[j+k] = True
        
        if now[j] > now[j-1]:
            
            for k in range(l):
                if j-1-k < 0 or visited[j-1-k] or now[j-1] != now[j-1-k]: # 1, 3, 4 조건
                    return False
                if now[j-1] == now[j-1-k]:
                    visited[j-1-k] = True
                    
    return True


for i in range(n):
    visited = [False for _ in range(n)]
    if check(data[i]):
        result += 1

for i in range(n):
    visited = [False for _ in range(n)]
    if check([data[j][i] for j in range(n)]):
        result += 1

print(result)
