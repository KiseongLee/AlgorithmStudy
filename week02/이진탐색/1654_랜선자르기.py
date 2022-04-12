n, k = map(int, input().split())

data=[]
for i in range(n):
    data.append(int(input()))
    
data.sort()

start = 1
end = data[-1]
ans = 0

while start <= end:
    
    mid = (start+end)//2
    
    
    if sum([i//mid for i in data]) >= k:            # 작거나 같다, 크거나 같다 이거 설정하는 게 key point이다
                                                    # 여기서는 최소 값의 개수를 만들어야 하므로 k보다 큰 쪽으로 설정을 해야 오류가 나지 않는다.
        start = mid + 1
        ans = mid
        
    else:
        end = mid -1

print(ans)