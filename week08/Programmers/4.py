#https://rain-bow.tistory.com/30

n = int(input())
lost = list(map(int, input().split()))
reserve = list(map(int, input().split()))

# ans = n - len(lost)
# for x in reserve:
#     if x-1 in lost:
#         lost.remove(x-1)
#     if x+1 in lost:
#         lost.remove(x+1)
    

# ans = n - len(lost)
# print(ans)


ans = n-len(lost)

for x in reserve:
    if x in lost:
        lost.remove(x)
        reserve.remove(x)
        ans += 1
        
for x in reserve:
    if x-1 in lost or x+1 in lost:
        ans += 1
    if ans >= n:
        ans = n
        break
    
print(ans)



# def solution(n, lost, reserve):
#     lost.sort()
#     reserve.sort()
#     ans = n - len(lost)
    
#     for x in reserve:
#         if x in lost:
#             lost.remove(x)
#             ans += 1
#             continue
#         if x-1 in lost or x+1 in lost:
#             ans += 1
#         if ans >= n:
#             ans = n
#             break
    
#     return ans

