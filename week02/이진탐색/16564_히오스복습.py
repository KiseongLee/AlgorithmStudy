n, k = map(int, input().split())

data = []
for i in range(n):
    data.append(int(input()))

data.sort()

start = data[0]
end = data[n-1]
ans = 0

def check(level):
    
    result = 0
    for i in range(len(data)):
        if level > data[i]:
            result += level - data[i]
    
    return result


while start <= end:
        
    mid = (start+end)//2
        
    if check(mid) <= k:
       ans = mid
       start = mid + 1
        
    else:
       end = mid - 1

print(ans)

