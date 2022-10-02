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


# 2022.09.01 복습
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def dfs(depth):
            
            if depth == len(nums):
                results.append(result[:])
            
            for i in range(len(nums)):
                if not visited[i]:
                    result[depth] = nums[i]
                    visited[i] = 1
                    dfs(depth+1)
                    visited[i]=0
        
        result = [0]*len(nums)
        results = []
        visited =[0]*len(nums)
        dfs(0)
        return results


# result 선언 후 값을 변경하기
# visited 활용

# 1. 재귀 종료 조건
# 2. for문 돌면서 depth 증가시키고 visited 1 -> 0으로 변환
# 주의) dfs 값 플러스할 때, depth로 증가시켜야함. 아니면 안돼