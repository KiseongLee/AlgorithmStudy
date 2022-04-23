def getMinOperation():
    global N, dist, path
 
    for i in range(2, N+1):
        dist[i] = dist[i-1] + 1
        path[i] = i-1
 
        if i % 2 == 0 and dist[i//2] + 1 < dist[i]:
            dist[i] = dist[i//2] + 1
            path[i] = i//2
 
        if i % 3 == 0 and dist[i//3] + 1 < dist[i]:
            dist[i] = dist[i//3] + 1
            path[i] = i//3
 
    print(dist[N])
 
 
def getpath():
    global N, path
 
    here = N
    while here != 0:
        print(here, end=' ')
        here = path[here]
        
 
if __name__ == '__main__':
    N = int(input())
    dist = [0 for _ in range(N+1)]
    path = [0 for _ in range(N+1)]
 
    getMinOperation()
    getpath()
    print(path)