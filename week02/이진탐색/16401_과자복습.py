

n, m = map(int, input().split())

food = list(map(int, input().split()))

start, end = 1, max(food)
ans = 0

while start <= end:
    
    mid = (start+end)//2
    
    
    if sum([n//mid for n in food]) >= m:    #sum할 때, 리스트화 해주지 않으면 값이 한개씩 들어가기 때문에 오류가 난다 참고
       ans = mid
       start = mid + 1
    
    else:
        end = mid - 1
        
print(ans) 
