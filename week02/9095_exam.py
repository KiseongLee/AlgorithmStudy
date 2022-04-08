# 중복 순열 문제네

array = [1, 2, 3]
t = int(input())


for _ in range(t):
    
    n = int(input())
    visited = []
    count = 0
    sum = 0
    def per(value, visited, depth):
        global count,sum
    
        if sum == n:
            # print(visited)        
            count+=1
            return
        
        if sum > n:
            return
        
        if depth == 0:
            return
        
        
        for i in range(len(array)):
            
                visited.append(array[i])
                sum += array[i]
                per(value+array[i], visited, depth)
                sum -= array[i]
                visited.pop()
                
    per(0, visited, n)
    print(count)

    


# n = int(input())

# arr = list(map(int, input().split()))
# visited = []
# count = 0

# def dfs(value):
#     global count
    
#     if len(visited) == len(arr):
#         print(visited)
#         count += 1
#         return
    
    
#     for i in range(len(arr)):
#         visited.append(arr[i])
        
#         dfs(value+arr[i])
        
#         visited.pop()
        

# dfs(0)
# print(count)