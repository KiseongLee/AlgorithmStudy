t = int(input())


for i in range(t):
    
    n, m = map(int, input().split())
    array = list(map(int, input().split()))
    data = []
    d = [[0]*m for i in range(n)]
    # print(d)
    for i in range(n):
        data.append(array[m*i:m*i+4])
        
    for i in range(n):
        d[i][0] = data[i][0]
    
    for j in range(1, m):
        for i in range(n):
        
            if i == 0:
                d[i][j] = max(d[i][j-1]+data[i][j], d[i+1][j-1]+data[i][j])
            
            elif i == n-1:
                d[i][j] = max(d[i-1][j-1]+data[i][j], d[i][j-1]+data[i][j])
                
            else:
                d[i][j] = max(d[i-1][j-1]+data[i][j], d[i][j-1]+data[i][j], d[i+1][j-1]+data[i][j])

    # print(d)
    ans = []
    for i in range(n):
        ans.append(d[i][m-1])
        
    print(max(ans))