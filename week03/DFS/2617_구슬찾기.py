def dfs(graph, v):
    
    global result
   
    result.append(v)
    
    for i in graph[v]:

        dfs(graph, i)
        
        
        

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
start = set()
result = []

for i in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)
    start.add(b)
    


for i in start:
    dfs(graph, i)
    print(result)
    result =[]
