n = int(input())
data = list(map(int, input().split()))

operator = list(map(int, input().split()))

visited = [False] * n
visited[0] = True
ans = []
def dfs(data, total, plus, minus, mul, div, visited):
    
    
    if all(visited) :
        ans.append(total)
        return ans
        
    
    for i in range(1, len(data)):
      if not visited[i]:
        visited[i] = True  
        if plus: dfs(data, total+data[i], plus-1, minus, mul, div, visited)
        if minus: dfs(data, total-data[i], plus, minus-1, mul, div, visited)
        if mul: dfs(data, total*data[i], plus, minus, mul-1, div, visited)
        if div: dfs(data, int(total/data[i]), plus, minus, mul, div-1, visited)
        visited[i] = False
        

dfs(data, data[0], operator[0], operator[1], operator[2], operator[3], visited)
print(max(ans))
print(min(ans))