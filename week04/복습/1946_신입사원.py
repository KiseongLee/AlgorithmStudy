t = int(input())

for i in range(t):
    n = int(input())
    
    data=[]
    for i in range(n):
        a, b = map(int, input().split())
        data.append((a,b))
    data.sort()
    
    X = data[0][1]
    cnt = 1
    for i in range(1, n):
            
            if X >= data[i][1]:
                X = data[i][1]
                cnt += 1
            
    print(cnt)