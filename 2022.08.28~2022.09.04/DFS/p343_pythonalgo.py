results = []
prev_elements =[]
    
def dfs(x):
    
    if len(nums) == x:
        results.append(result[:])
    
    for i in range(len(nums)):
        if visited[i] == False:
            result[x]=nums[i]
            visited[i]=True
            dfs(x+1)
            visited[i]=False

nums=[1,2,3]
result = [0]*len(nums)
visited = [0]*len(nums)
dfs(0)
print(results)