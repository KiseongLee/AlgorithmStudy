import collections
pre = [[1,2],[3,4],[2,3],[4,5]]
graph = collections.defaultdict(list)
for a,b in pre:
    graph[a].append(b)
        
visited = set()
traced = set()
        
def dfs(x):
    
    if x in traced:
        return False
    
    if x in visited:
        return True
    
    traced.add(x)
    for y in graph[x]:
        if not dfs(y):
            return False
    traced.remove(x)
    visited.add(x)
    
    return True

print(graph)
print(list(graph)) # 키 값만 뽑아내는 것이구만
for x in list(graph):
    if not dfs(x):
        print(False)
print(True)