n, k = map(int, input().split())

data = []
for i in range(n):
    data.append(int(input()))

data.sort()     # sort 중요

start = 1
end = data[-1]
ans = 0

def binary_search(target, start, end):      # 굳이 함수로 안해도 된다. 시간만 더 잡아먹음
    
    global ans
    
    while start <= end:
        
        mid = (start+end)//2
        
        if  sum(l//mid for l in data) >= target:
            ans = mid
            start = mid + 1
            
        else:
            end = mid - 1
    return ans

print(binary_search(k, start, end))
