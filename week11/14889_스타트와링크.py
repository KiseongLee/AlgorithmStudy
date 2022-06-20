# from itertools import permutations


# n = int(input())

# data = [list(map(int,input().split())) for _ in range(n)]

# data_sum = []
# for i in range(n):
#     for j in range(i+1, n):
#         data_sum.append(data[i][j]+data[j][i])

# print(data_sum)        


# min_value = 1e9
# for i in range(len(data_sum)//2):
#     min_value = min(min_value, abs(data_sum[i]-data_sum[-i-1]))

# print(min_value)

# a=[]
# for i in range(n):
#     a.append(i+1)

# a_permu = list(permutations(a, len(a)))
# print(a_permu)
# a_list = [[] for _ in range(len(a_permu))]
# print(a_list)
# for i in range(len(a_permu)):
    
#     a_list[i].append(a_permu[i][0:len(a)//2])
#     a_list[i].append(a_permu[i][len(a)//2:])

# print(a_list)

# 백트래킹으로 접근

# dfs로 n//2 될 때까지 돌려 visited가 나누기 2가 됨
# 바로 visited for문으로 전부 돌린다. 전체 행렬을 도는 것이고 
# 두 개가 같은 visited 상태일 때만 더해준다.
# 최솟값을 갱신해준다.

import sys
input = sys.stdin.readline

n = int(input())
data = [list(map(int,input().split())) for _ in range(n)]
visited = [False]*(n)
min_value = 1e9

def dfs(depth, idx):
    global min_value
    
    if depth == n//2:
        
        start, link = 0, 0
        
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    start += data[i][j]
                if not visited[i] and not visited[j]:
                    link += data[i][j]
        
        diff = abs(start-link)
        if min_value > diff:
            min_value = diff
          
    for i in range(idx, n):
       if not visited[i]:
           visited[i] = True
           dfs(depth+1, i+1)
           visited[i] = False
           
dfs(0, 0)
print(min_value)


