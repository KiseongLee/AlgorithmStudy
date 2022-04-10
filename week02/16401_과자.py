

n, m = map(int, input().split())

data = list(map(int, input().split()))

data.sort()


def check(height):
    result = 0
    for i in range(m):
        if data[i] >= height:
            result += data[i] // height
        
    return result
        
def binary_sort(target, start, end):
    
    if n > sum(data):
        return 0

    while start <= end:
        
        mid = (start+end)//2
        
        get = check(mid)
        
        if get >= target:
            
            start = mid + 1 
    
        else:
            
            end = mid -1
            
    return end


print(binary_sort(n, 0, data[m-1]))


# M, N = map(int, input().split())
# li = list(map(int, input().split()))
# s, e = 1, max(li)
# res = 0
# while s <= e:
#     m = (s+e)//2
#     if sum([n//m for n in li]) >= M:
#         res = m
#         s = m+1
#     else:
#         e = m-1
# print(res)